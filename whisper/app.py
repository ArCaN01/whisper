from flask import Flask, request, render_template, redirect, url_for
from web3 import Web3
import ipfshttpclient
import json

app = Flask(__name__)

# Инициализация Web3
infura_url = 'https://mainnet.infura.io/v3/841b6bcee7354760bbc65a584107181d'
web3 = Web3(Web3.HTTPProvider(infura_url))

# Подключение к IPFS
client = ipfshttpclient.connect('/ip4/127.0.0.1/tcp/5001')

# Загрузка ABI контракта
with open('TwitterABI.json') as f:
    contract_abi = json.load(f)

contract_address = '0xd9145CCE52D386f254917e481eB44e9943F39138'
twitter_contract = web3.eth.contract(address=contract_address, abi=contract_abi)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/tweet', methods=['POST'])
def tweet():
    message = request.form['message']
    tweet_data = {
        'message': message,
        'timestamp': request.form['timestamp']
    }
    res = client.add_json(tweet_data)
    ipfs_hash = res['Hash']
    tx_hash = twitter_contract.functions.postTweet(ipfs_hash).transact()
    web3.eth.waitForTransactionReceipt(tx_hash)
    return redirect(url_for('get_tweets'))

@app.route('/tweets')
def get_tweets():
    tweets = twitter_contract.functions.getTweets().call()
    tweets_data = []
    for tweet in tweets:
        ipfs_data = client.cat(tweet[1])
        tweets_data.append(json.loads(ipfs_data))
    return render_template('tweets.html', tweets=tweets_data)

if __name__ == '__main__':
    app.run(debug=True)