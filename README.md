## PEP parser

## Описание
Парсер для сбора статистики по дукументам PEP<br/>
Формирует 2 файла с данными в формате .csv при помощи фреймворка scrapy<br/>
Отчеты:
1. Перачень всех PEP. Данные: «Номер», «Название» и «Статус».  
2. Cводка по статусам PEP. Данные: «Статус» и «Количество».

## Как получить отчет
1. git clone git@github.com:helhander/pep-parser.git
2. cd pep-parser
3. python -m venv venv
4. source ./venv/Scripts/activate
5. pip install -r requirements.txt
6. scrapy crawl pep
7. Отчеты появятся в папке ./results/
