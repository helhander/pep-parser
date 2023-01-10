import csv
from datetime import datetime
from pep_parse.settings import BASE_DIR


class PepParsePipeline:
    def open_spider(self, spider):
        self.pep_statuses_counter = {}

    def process_item(self, item, spider):
        status = item['status']
        self.pep_statuses_counter[status] = (
            self.pep_statuses_counter.get(status, 0) + 1
        )
        return item

    def close_spider(self, spider):
        today = datetime.utcnow()
        date_string = f'{today:%Y-%m-%dT%H-%M-%S}'
        with open(
            f'{BASE_DIR}/results/status_summary_{date_string}.csv',
            'w',
            newline='',
            encoding='utf-8',
        ) as csvfile:
            fieldnames = ['Статус', 'Количество']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            status_total = 0
            for status, number in self.pep_statuses_counter.items():
                writer.writerow({'Статус': status, 'Количество': number})
                status_total += number
            writer.writerow({'Статус': 'Total', 'Количество': status_total})
