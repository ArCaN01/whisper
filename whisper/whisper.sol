// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract Twitter {
    struct Tweet {
        address user;
        string ipfsHash;
        uint timestamp;
    }

    Tweet[] public tweets;

    event NewTweet(address indexed user, string ipfsHash, uint timestamp);

    function postTweet(string memory _ipfsHash) public {
        tweets.push(Tweet(msg.sender, _ipfsHash, block.timestamp));
        emit NewTweet(msg.sender, _ipfsHash, block.timestamp);
    }

    function getTweets() public view returns (Tweet[] memory) {
        return tweets;
    }
}