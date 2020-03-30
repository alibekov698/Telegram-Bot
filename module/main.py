# subprocess is an universal inteface for all types of systems
from subprocess import Popen, PIPE

from telebot import types
from telegram import Bot
from telegram import Update
from telegram import ParseMode, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, MessageHandler, CallbackQueryHandler

from config import TG_TOKEN

CALLBACK_BUTTON1_WORK = "callback_button1_work"
CALLBACK_BUTTON2_SUFFERING = "callback_button2_suffering"
CALLBACK_BUTTON3_RELATIONSHIPS = "callback_button3_relationships"
CALLBACK_BUTTON4_WORK_MORE = "callback_button4_work_more"
CALLBACK_BUTTON5_BACK = "callback_button6_back"
CALLBACK_BUTTON6_STEVE = "callback_button7_steve"
CALLBACK_BUTTON7_ELON = "callback_button8_elon"

TITLES = {
    CALLBACK_BUTTON1_WORK: "Work",
    CALLBACK_BUTTON2_SUFFERING: "Suffering",
    CALLBACK_BUTTON3_RELATIONSHIPS: "Relationships",
    CALLBACK_BUTTON4_WORK_MORE: "More",
    CALLBACK_BUTTON5_BACK: "Back",
    CALLBACK_BUTTON6_STEVE:"Steve Jobs",
    CALLBACK_BUTTON7_ELON: "Elon Musk",
}

def get_base_inlne_keyboard():
    keyboard = [
        [
            InlineKeyboardButton(TITLES[CALLBACK_BUTTON1_WORK], callback_data=CALLBACK_BUTTON1_WORK),
            InlineKeyboardButton(TITLES[CALLBACK_BUTTON2_SUFFERING],callback_data=CALLBACK_BUTTON2_SUFFERING),
        ],
        [
            InlineKeyboardButton(TITLES[CALLBACK_BUTTON3_RELATIONSHIPS],callback_data=CALLBACK_BUTTON3_RELATIONSHIPS),
        ],
    ]
    return InlineKeyboardMarkup(keyboard)

def get_keyboard_work():
    keyboard = [
        [
            InlineKeyboardButton(TITLES[CALLBACK_BUTTON4_WORK_MORE],callback_data=CALLBACK_BUTTON4_WORK_MORE),
        ],
        [
            InlineKeyboardButton(TITLES[CALLBACK_BUTTON5_BACK],callback_data=CALLBACK_BUTTON5_BACK),
        ],
    ]
    return InlineKeyboardMarkup(keyboard)

@bot.callback_query_handler(func=lambda c:True)
def keyboard_callback_handler(bot: Bot, update: Update):
    query = update.callback_query
    data = query.data
    if data == CALLBACK_BUTTON1_WORK:
        bot.edit_message_text(
            text = 'sdfdfs',
            #reply_markup=get_keyboard_work(),
        )


def do_work(bot: Bot, update: Update):
    update.message.reply_text(
        "_“The only way to do Great Work is to Love What You Do” (Steve Jobs)_",
        parse_mode=ParseMode.MARKDOWN,
    )

def do_start(bot: Bot, update: Update):
    bot.send_message(
        chat_id = update.message.chat_id,
        text = "Hi, I am a bot motivator.\n\n"
                "Think for a moment. What's your 'why' or what's your meaning of life?\n\n"
                "Is it hard to answer? Let me help you.\n"
                "For more information about 'why', write /why .\n"
                "To determine your 'why', write /therapy",
    )

def do_why(bot: Bot, update: Update):
    update.message.reply_text(
        "It will help you to get more knowledge about 'why' [here](https://www.youtube.com/watch?v=qp0HIF3SfI4)",
        parse_mode=ParseMode.MARKDOWN,
    )

def do_therapy(bot: Bot, update: Update):
    update.message.reply_text(
        "You can choose a therapy you prefer.\n"
        "_Mark Manson_ /mm \n"
        "_Logotherapy_ /logo",
        parse_mode=ParseMode.MARKDOWN,
    )

def do_mm(bot: Bot, update: Update):
    update.message.reply_text(
        "Mark Manson is the #1 NYTimes bestselling author of _The Subtle Art of Not Giving a F*ck_ [here](https://markmanson.net/life-purpose)",
        parse_mode=ParseMode.MARKDOWN,
    )

currencies = ['usd','euro']
def create_keyboard():
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    buttons = [types.InlineKeyboardButton(text=c,callback_data=c)
                for c in currencies]
    keyboard.add(*buttons)
    return keyboard

def do_logo(bot: Bot, update: Update):
    bot.send_message(
        chat_id = update.message.chat_id,
        text = "_“Logotherapy focuses on the search for the meaning of human existence” (Frankl, 1958)._\n\n"
                "*FINDING MEANING WITH LOGOTHERAPY:*\n\n"
                "1. *Work*: by creating a work or accomplishing some task.\n\n"
                "2. *Relationships*: by experiencing something fully or loving somebody.\n\n"
                "3. *Suffering*: by the attitude that one adopts toward unavoidable suffering.",
        parse_mode=ParseMode.MARKDOWN,
        reply_markup=get_base_inlne_keyboard(),
    )

def main():
    bot = Bot(
        token = TG_TOKEN
    )
    updater = Updater(
        token=TG_TOKEN,
    )

    start_handler = CommandHandler("start", do_start)
    why_handler = CommandHandler("why", do_why)
    therapy_handler = CommandHandler("therapy", do_therapy)
    mm_handler = CommandHandler("mm", do_mm)
    logo_handler = CommandHandler("logo", do_logo)

    updater.dispatcher.add_handler(start_handler)
    updater.dispatcher.add_handler(why_handler)
    updater.dispatcher.add_handler(therapy_handler)
    updater.dispatcher.add_handler(mm_handler)
    updater.dispatcher.add_handler(logo_handler)
    updater.dispatcher.add_handler(CallbackQueryHandler(callback=keyboard_callback_handler,pass_chat_data=True))

#launch of the program
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
