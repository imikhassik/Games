import telebot
from config import TOKEN


bot = telebot.TeleBot(TOKEN)

currencies = {'евро': 'EUR',
              'доллар': 'USD',
              'рубль': 'RUB'}


@bot.message_handler(commands=['start', 'help'])
def get_help(message: telebot.types.Message):
    text = '''Формат ввода:\n<какую валюту конвертировать> \
<в какую валюту конвертировать> <количество>'''
    bot.reply_to(message, text)


@bot.message_handler(commands=['values'])
def get_values(message: telebot.types.Message):
    text = 'Список возможных валют:'
    for value in currencies.keys():
        text = ('\n'.join([text, value]))
    bot.reply_to(message, text)


bot.polling()
