import telebot
import wikipedia

token = '7165090560:AAG_LJgA8B1GgpI0PrBTPBY_mLImfY3K4-8'
bot = telebot.TeleBot(token)

wikipedia.set_lang('ru')


def get_info(word):
    try:
        wikitext = wikipedia.page(word).content[:500]
        wikitext = wikitext.split('.')
        wikitext = '. '.join(wikitext[:-1]) + '.'
        return wikitext
    except Exception as e:
        return 'B ЭНЦИКЛОПЕДИИ HET ИНФОРМАТЦИИ OБ ЭТОМ'


@bot.message_handler(commands=['start'])
def start(message):
    message2 = bot.send_message(message.chat.id, 'Что вы хотите узнать из wikipedia')
    bot.register_next_step_handler(message2, handle_text)

def handle_text(message):
    word = message.text
    info = get_info(word)
    bot.send_message(message.chat.id, info)
    start(message)


bot.polling()



































































