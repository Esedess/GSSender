# Google Spreadsheets Sender

Добавляет строкой данные в конец указанной Google-таблицы.

***

### Как использовать:

Установить зависимости из файла requirements.txt:

```bash
python -m pip install --upgrade pip
```

```bash
pip install -r requirements.txt
```
Завести сервисный аккаунт на Google Cloud.
Дать сервисному аккаунту доступ к нужной таблице.

Наполнить .env по примеру .env_example.

Импортировать модуль в ваш код:

```bash
from GSSender import asyncio_sender
```

Пример необходимых переменных:

```bash
spreadsheetid = '1v-1Ky1r11LyDGsBZEJ1vwtjncQIneeIP1uVYkZxkyyc'
values = [
    ['Пример 1'],
    ['Пример 2'],
    ['Пример 3'],
    ['Пример 4'],
]
```

Запустить:

```bash
asyncio_sender(spreadsheetid, values)
```

***

## Tech Stack

+ `Python` : <https://github.com/python>
+ `aiogoogle` : <https://github.com/omarryhan/aiogoogle>


***

## Авторы

- [@Esedess](https://github.com/Esedess)
