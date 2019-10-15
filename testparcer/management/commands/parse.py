from django.core.management.base import BaseCommand
import urllib.request
import re


class Command(BaseCommand):
    target_url = 'http://www.almhuette-raith.at/apache-log/access.log'
    data = urllib.request.urlopen(target_url)
    pattern = r'(\S+) (\S+) (\S+) \[(.*?)\] \"(\S+) (.*?) (\S+)\" (\S+) (\S+) (\".*?\") (\".*?\")'
    total_length = data.length#кол-во байт в ответе
    temp_percent = 0#вычисленный процент временный
    temp_length = 0#кол-во байт в итерации
    count = 0
    for line in data:
        count += 1
        temp_length += len(line.decode('utf-8'))
        current_percent = int((temp_length/total_length)*100)
        if current_percent != temp_percent:
            temp_percent = current_percent
            print(str(current_percent) + '%')

        if count % 10000 == 0:
            # print(count)
            result = re.findall(pattern, str(line))
            # print(result)
    print(count)

    def reader(self):
        pass

    def handle(self, *args, **options):
        pass
