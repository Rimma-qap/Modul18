# Модуль 18

Написать и протестировать Telegram-бота, в котором будет реализован 
следующий функционал:
1. Бот возвращает цену на определённое количество валюты 
(евро, доллар или рубль).
1. При написании бота необходимо использовать библиотеку `pytelegrambotapi`.
1. Человек должен отправить сообщение боту в виде 
**<имя валюты цену, которой он хочет узнать>** 
**<имя валюты, в которой надо узнать цену первой валюты>** 
**<количество первой валюты>**.
1. При вводе команды `/start` или `/help` пользователю выводятся инструкции 
по применению бота.
1. При вводе команды `/values` должна выводиться информация о всех доступных 
валютах в читаемом виде.
1. Для взятия курса валют необходимо использовать 
[API](https://www.cryptocompare.com/) и отправлять к нему запросы с помощью 
библиотеки `Requests`.
1. Для парсинга полученных ответов использовать библиотеку `JSON`.
1. При ошибке пользователя (например, введена неправильная или несуществующая 
валюта или неправильно введено число) вызывать собственно написанное исключение 
`APIException` с текстом пояснения ошибки.
1. Текст любой ошибки с указанием типа ошибки должен отправляться пользователю 
в сообщения.
1. Для отправки запросов к API описать класс со статическим методом 
`get_price()`, который принимает три аргумента: имя валюты, цену на которую 
надо узнать, — `base`, имя валюты, цену в которой надо узнать, — `quote`, 
количество переводимой валюты — `amount` и возвращает нужную сумму в валюте.
1. Токен *telegramm-бота* хранить в специальном конфиге (можно использовать 
`.py` файл).
1. Все классы спрятать в файле `extensions.py`.