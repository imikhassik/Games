import telebot


from config import TOKEN, currencies


bot = telebot.TeleBot(TOKEN)


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


@bot.message_handler(content_types=['text'])
def get_input(message: telebot.types.Message):
    user_input = message.text.split(' ')
    base, quote, amount = user_input[0], user_input[1], user_input[2]


bot.polling()
