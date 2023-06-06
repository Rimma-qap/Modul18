import telebot

from config import keys, TOKEN
from extensions import APIException, CryptoConverter

bot = telebot.TeleBot(TOKEN)

HELP_TEXT = '''
Чтобы начать работу введите команду боту в следующем формате:

<Валюта1> <Валюта2> <Количество>

где <Валюта1> - название валюты, цену которой хотите узнать 
<Валюта2> - название валюты, в которой надо узнать цену первой валюты
<Количество> - количество <Валюта1>

Например, доллар рубль 123

Увидеть список всех доступных валют: /values
'''


@bot.message_handler(commands=['start'])
def start(message: telebot.types.Message):
    text = f'Привет, {message.chat.username}!\n{HELP_TEXT}'
    bot.reply_to(message, text)


@bot.message_handler(commands=['help'])
def help(message: telebot.types.Message):
    bot.reply_to(message, HELP_TEXT)


@bot.message_handler(commands=['values'])
def values(message: telebot.types.Message):
    text = 'Доступные валюты:'
    for key in keys.keys():
        text = '\n'.join((text, key,))
    bot.reply_to(message, text)


@bot.message_handler(content_types=['text'])
def convert(message: telebot.types.Message):
    try:
        values = message.text.split(' ')

        if len(values) != 3:
            raise APIException('Слишком много параметров.')

        quote, base, amount = values
        total_base = CryptoConverter.get_price(quote, base, amount)
    except APIException as e:
        bot.reply_to(message, f'Ошибка пользователя.\n{e}')
    except Exception as e:
        bot.reply_to(message, f'Не удалось обработать команду\n{e}')
    else:
        text = f'Цена {amount} {quote} в {base} - {total_base}'
        bot.send_message(message.chat.id, text)


bot.polling()
