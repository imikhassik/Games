import telebot
from config import TOKEN


bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start', 'help'])
def help_func(message: telebot.types.Message):
    text = '''Формат ввода:\n<какую валюту конвертировать> \
<в какую валюту конвертировать> <количество>'''
    bot.reply_to(message, text)


bot.polling()
