import telebot
from telebot import types
from telegram import ParseMode
from config import TG_TOKEN

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
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    buttons = [types.InlineKeyboardButton(text=i, callback_data=i) for i in logo_types]
    keyboard.add(*buttons)
    return keyboard

@bot.callback_query_handler(func=lambda x:True)
def keyboard_handler(callback_query):
    keyboard_back = types.InlineKeyboardMarkup()
    button = types.InlineKeyboardButton(text='Back',callback_data='Work')
    keyboard_back.add(button)

    if callback_query.data == 'Work':
        keyboard = types.InlineKeyboardMarkup(row_width=1)
        steve_url = types.InlineKeyboardButton(text='Steve\'s Motivational Video',url='https://www.youtube.com/watch?v=ptD0T-ZcF2M')
        elon_url = types.InlineKeyboardButton(text='Elon\'s Motivational Video',url='https://www.youtube.com/watch?v=k9zTr2MAFRg&t=358s')
        steve_life = types.InlineKeyboardButton(text='Steve\'s Principles of Life',callback_data='Steve\'s Principles of Life')
        elon_life = types.InlineKeyboardButton(text='Elon\'s Principles of Life',callback_data='Elon\'s Principles of Life')
        keyboard.add(steve_url,steve_life,elon_url,elon_life)
        bot.send_message(chat_id = callback_query.message.chat.id,
                    text = "_“The only way to do Great Work is to Love What You Do” (Steve Jobs)._",
                    parse_mode=ParseMode.MARKDOWN, reply_markup = keyboard)
    elif callback_query.data == 'Suffering':
        keyboard_suffering = types.InlineKeyboardMarkup()
        suffering_stories = types.InlineKeyboardButton(text='Finding Meaning in Suffering',url='https://pro.psychcentral.com/finding-meaning-in-suffering/')
        keyboard_suffering.add(suffering_stories)
        bot.send_message(chat_id = callback_query.message.chat.id,
                    text = "_“No victory without suffering” (J. R. R. Tolkien)._",
                    parse_mode=ParseMode.MARKDOWN,reply_markup=keyboard_suffering)
    elif callback_query.data == 'Relationships':
        keyboard_rel = types.InlineKeyboardMarkup()
        muslim = types.InlineKeyboardButton(text='Muslim Spoken Word',url='https://www.youtube.com/watch?v=7d16CpWp-ok')
        love = types.InlineKeyboardButton(text='Love & Marriage', url='https://www.youtube.com/watch?v=fPstjtUTsHE')
        keyboard_rel.add(muslim,love)
        bot.send_message(chat_id = callback_query.message.chat.id,
                    text = "_“The best and most beautiful things in the world cannot be seen or even heard, but must be felt with the Heart” (Helen Keller)._",
                    parse_mode=ParseMode.MARKDOWN,reply_markup=keyboard_rel)
    elif callback_query.data == 'Steve\'s Principles of Life':
        bot.edit_message_text(chat_id=callback_query.message.chat.id,
                message_id=callback_query.message.message_id,
                    text = '_7 Principles Behind Steve Jobs_\n\n'
                        '1. _Do what you love_.\nThink differently about your career. Steve Jobs followed his heart his entire life and that, he said, made all the difference. Innovation cannot occur in the absence of passion and, without it, you have little hope of creating breakthrough ideas.\n\n'
                        '2. _Sell dreams, not products_.\nThink differently about your customers. To Jobs, people who bought Apple products were never “consumers.” They were people with dreams, hopes, and ambitions. Jobs built products to help them fulfill their dreams.\n\n'
                        '3. _Don’t be shy to learn from others_.\nIf you feel like you are stuck in certain areas of your life, do not hesitate to ask for help from the experts. Sometimes that little help is all you need to start getting results and be successful.\n\n'
                        '4. _Remember you’ll be dead soon_.\nWhen you are confused, scared, embarrassed, or anything, just remember that you’ll be dead soon. Life is short; so make sure that you make it count.\n\n'
                        '5. _Fail forward_.\n We should not fear failure, because failure is not the end of the road. We must take failure as the opportunity to learn and improve ourselves, and success is inevitable.\n\n'
                        '6. _Take risks_.\nMost of the time, we need to take risks in order to move forward. Just be careful and make sure that the risk that you took was a calculated risk. Think thoroughly, weigh the best and worse scenarios of an action against each other, and then you can decide whether the risk is worth taking.\n\n'
                        '7. _Travel the world_.\nA simple weekend getaway to another city nearby might be enough for you to experience new things and broaden your horizon.',
                    parse_mode=ParseMode.MARKDOWN, reply_markup=keyboard_back)
    elif callback_query.data == 'Elon\'s Principles of Life':
        bot.edit_message_text(chat_id=callback_query.message.chat.id, message_id=callback_query.message.message_id,
                    text = '_Success Principles from Elon Musk_\n\n'
                        '1. _Work Extremely Hard_.\nWork like hell. I mean you just have to put in 80 to 100 hour weeks every week. If other people are putting in 40 hour work weeks and you’re putting in 100 hour work weeks, then even if you’re doing the same thing you know that… you will achieve in 4 months what it takes them a year to achieve.\n\n'
                        '2. _Dare to Take Risk_.\nOnce you have a family it gets much harder to do things that might not work out.\n\n'
                        '3. _Never be Afraid to Fail_.\nIf something is important enough you should try even if the probable outcome is a failure. When you are afraid to fail, you will hold back and never dare to do something to your full potential.\n\n'
                        '4. _Always be Learning_.\nIf you want to be successful and produce outstanding results in your life, equip yourself with knowledge. Make it a habit to read and turn on your commitment to consistent learning each and every day.\n\n'
                        '5. _Turn Criticism into Feedback_.\nIt’s important for people to pay close attention to negative feedback and rather than ignore negative feedback, you have to listen to it carefully. Ignore it if the underlying reason for the negative feedback doesn’t make sense but otherwise, people should adjust their behavior.\n\n'
                        '6. _Think Out of the Box_.\nDo not be afraid to think out of the box. Do not follow the trend, instead, become the trendsetter and be the first one to venture into something new. If you want to reap the greatest reward, you will have to focus on innovation rather than competition.\n\n'
                        '7. _Enjoy Life and Celebrate Success_.\nSometimes you just need to let go and enjoy life. Life is supposed to be fun and not just about work or business. You need to learn how to let go and pamper yourself with joyful activities that you truly enjoy. Take it as a task to recharge and refresh yourself.',
                    parse_mode=ParseMode.MARKDOWN, reply_markup=keyboard_back)

if __name__ == '__main__':
    bot.infinity_polling()
