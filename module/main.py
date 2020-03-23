from telegram import Bot
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

from config import TG_TOKEN

def do_start(bot: Bot, update: Update):
    #sending messages
    bot.send_message(
        chat_id = update.message.chat_id,
        text = "Hi, my friend! Would you like to send me something?",
    )
#process all incoming messages
def do_echo(bot: Bot, update: Update):
    chat_id = update.message.chat_id
    text = "Your ID is = {}\n\n{}".format(chat_id, update.message.text)
    bot.send_message(
        chat_id=update.message.chat_id,
        text=text,
    )

def main():
    bot = Bot(
        token = TG_TOKEN
    )
    updater = Updater(
        bot = bot,
    )

    start_handler = CommandHandler("start", do_start)
    message_hadler = MessageHandler(Filters.text, do_echo)
    updater.dispatcher.add_handler(start_handler)
    updater.dispatcher.add_handler(message_hadler)

#launch of the program
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
