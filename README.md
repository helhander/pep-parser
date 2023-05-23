# PEP parser
## Описание
Парсер предназначен для сбора статистики по дукументам PEP<br/>
Формирует 2 файла с данными в формате .csv при помощи фреймворка scrapy<br/>
Отчеты:
1. Перачень всех PEP. Данные: «Номер», «Название» и «Статус».  
2. Cводка по статусам PEP. Данные: «Статус» и «Количество».

## Как получить отчет
1. clone git@github.com:helhander/scrapy_parser_pep.git
2. cd scrapy_parser_pep
3. python -m venv venv
4. source ./venv/Scripts/activate
5. pip install -r requirements.txt
6. scrapy crawl pep
7. Отчеты появятся в папке ./results/

## Автор
Трофимов Никита
