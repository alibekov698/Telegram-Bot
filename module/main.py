# subprocess is an universal inteface for all types of systems
from subprocess import Popen, PIPE

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

def do_help(bot: Bot, update: Update):
    #sending messages
    bot.send_message(
        chat_id = update.message.chat_id,
        text = "I am an advisor\n"
                "The list of the commands are available in the menu\n"
                "Also, I can answer on any questions",
    )

def do_time(bot: Bot, update: Update):
    process = Popen(["date"], stdout=PIPE)
    text, error = process.communicate() # we want to wait the result
    if error:
        text = "Error was happening, time is unfamiliar"
    else:
        text = text.decode("utf-8") #to decode bytes
    bot.send_message(
        chat_id = update.message.chat_id,
        text = text,
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
    help_handler = CommandHandler("help", do_help)
    time_handler = CommandHandler("time", do_time)
    message_hadler = MessageHandler(Filters.text, do_echo)

    updater.dispatcher.add_handler(start_handler)
    updater.dispatcher.add_handler(help_handler)
    updater.dispatcher.add_handler(time_handler)
    updater.dispatcher.add_handler(message_hadler)

#launch of the program
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
