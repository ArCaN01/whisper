from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

def start(update: Update, context: CallbackContext):
    update.message.reply_text('Привет! Я Web3 Twitter бот. Используйте команду /webapp для доступа к веб-приложению.')

def webapp(update: Update, context: CallbackContext):
    update.message.reply_text('Нажмите на ссылку, чтобы открыть веб-приложение: https://your-web-app-url.com')

def main():
    updater = Updater('7493621353:AAE0eOwvzaDUwlvq47Ic9G_Tm_bnHCqv0kk', use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("webapp", webapp))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
