import telebot

from config import keys, TOKEN
from extensions import APIException, CryptoConverter

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def start(message: telebot.types.Message):
    text = f'''Привет, {message.chat.username}!
    Я Бот - Валютный калькулятор - @Calc_ValutaBot.
    Помогу быстро перевести любую сумму из одной валюты в другую.
    Просто напиши какую валюту хочешь перевести в какую и его количество.
    
    Например, необходимо перевести 100 евро в рубли.
    Вводим: евро рубль 100
    Получаем ответ: Стоимость 100 евро равен 8752.0 рубль
    
    Краткая инструкция по использованию бота - /help
    Список всех доступных валют - /values
    Приветствие бота - /start'''

    bot.reply_to(message, text)


@bot.message_handler(commands=['help'])
def help(message: telebot.types.Message):
    text = '''Чтобы начать работу введите команду боту в следующем формате:
    
    <Валюта1> <Валюта2> <Количество>, где
    
    <Валюта1> - Название валюты, которую необходимо перевести
    <Валюта2> - Название валюты, в которую конвертируется <Валюта 1>
    <Количество> - Количество валют <Валюта1>, необходимых перевести в <Валюта2>
    
    Например, необходимо перевести 100 евро в рубли.
    Вводим: евро рубль 100
    Получаем ответ: Стоимость 100 евро равен 8752.0 рубль
    
    Краткая инструкция по использованию бота - /help
    Список всех доступных валют - /values
    Приветствие бота - /start'''

    bot.reply_to(message, text)


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
            raise APIException('''Некорректный ввод данных!
            Пример правильного ввода данных: евро рубль 100 
            Получим ответ: Стоимость 100 евро равен 8747.0 рубль''')

        quote, base, amount = values
        total_base = CryptoConverter.get_price(quote, base, amount)
        total_base = round(total_base, 2)
    except APIException as e:
        bot.reply_to(message, f'Ошибка пользователя!\n{e}')
    except Exception as e:
        bot.reply_to(message, f'Не удалось обработать команду:\n{e}')
    else:
        text = f'Стоимость {amount} {quote} равен {total_base} {base}'
        bot.send_message(message.chat.id, text)


bot.polling()
