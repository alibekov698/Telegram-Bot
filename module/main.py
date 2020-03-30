import telebot
from telebot import types
from telegram import ParseMode
from config import TG_TOKEN
'''
    CALLBACK_BUTTON6_STEVE:"Steve Jobs",
    CALLBACK_BUTTON7_ELON: "Elon Musk",
'''
bot = telebot.TeleBot(TG_TOKEN)

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(chat_id=message.chat.id,
        text = "Hi, I am a bot motivator.\n\n"
            "Think for a moment. What's your 'why' or what's your meaning of life?\n\n"
            "Is it hard to answer? Let me help you.\n"
            "For more information about 'why', write /why .\n"
            "To determine your 'why', write /therapy")

@bot.message_handler(commands=['therapy'])
def therapy_message(message):
    bot.send_message(chat_id = message.chat.id,
        text = "You can choose a therapy you prefer.\n"
                "_Mark Manson_ /mm \n"
                "_Logotherapy_ /logo",
        parse_mode=ParseMode.MARKDOWN)

@bot.message_handler(commands=['why'])
def why_message(message):
    bot.send_message(chat_id=message.chat.id,
        text = "It will help you to get more knowledge about 'why' [here](https://www.youtube.com/watch?v=qp0HIF3SfI4)",
        parse_mode=ParseMode.MARKDOWN,)

@bot.message_handler(commands=['mm'])
def mm_message(message):
    bot.send_message(chat_id = message.chat.id,
        text = "Mark Manson is the #1 NYTimes bestselling author of _The Subtle Art of Not Giving a F*ck_ [here](https://markmanson.net/life-purpose)",
        parse_mode = ParseMode.MARKDOWN)

@bot.message_handler(commands=['logo'])
def do_logo(message):
    bot.send_message(chat_id = message.chat.id,
        text = "_“Logotherapy focuses on the search for the meaning of human existence” (Frankl, 1958)._\n\n"
                "*FINDING MEANING WITH LOGOTHERAPY:*\n\n"
                "1. *Work*: by creating a work or accomplishing some task.\n\n"
                "2. *Relationships*: by experiencing something fully or loving somebody.\n\n"
                "3. *Suffering*: by the attitude that one adopts toward unavoidable suffering.",
        parse_mode = ParseMode.MARKDOWN,
        reply_markup = logo_keyboard())

logo_types = ['Work','Suffering','Relationships']
def logo_keyboard():
    keyboard = types.InlineKeyboardMarkup(row_width=3)
    buttons = [types.InlineKeyboardButton(text=i, callback_data=i) for i in logo_types]
    keyboard.add(*buttons)
    return keyboard

work = ['More','Back']
def work_keyboard():
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    buttons = [types.InlineKeyboardButton(text=i, callback_data=i) for i in work]
    keyboard.add(*buttons)
    return keyboard

@bot.callback_query_handler(func=lambda x:True)
def work_handler(callback_query):
    message = callback_query.message
    bot.send_message(chat_id = message.chat.id,
            text = "_“The only way to do Great Work is to Love What You Do” (Steve Jobs)_",
            parse_mode=ParseMode.MARKDOWN,
            reply_markup = work_keyboard())

bot.polling()
