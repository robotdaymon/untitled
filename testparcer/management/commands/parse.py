import os
from django.core.management.base import BaseCommand
import urllib.request
import re
import datetime
from testparcer.models import Parceline, Badstring
from untitled.settings import BASE_DIR


class Command(BaseCommand):
    filename = BASE_DIR + '\\parsed-logs\\'
    print(filename)
    if not os.path.exists(filename):
        os.makedirs(filename)
    filename += str(datetime.datetime.now().strftime('%d-%B-%Y %H.%M.%S')) + '.log'
    print(type(filename))
    print(filename)
    tmpfile = open(str(filename), 'w')
    target_url = 'http://www.almhuette-raith.at/apache-log/access.log'
    data = urllib.request.urlopen(target_url)
    pattern = r'(\S+) (\S+) (\S+) \[(.*?)\] \"(\S+) (.*?) (\S+)\" (\S+) (\S+) (\".*\") (\".*?\") (\".*?\")'
    total_length = data.length#кол-во байт в ответе
    temp_percent = 0#вычисленный процент временный
    temp_length = 0#кол-во байт в итерации
    count = 0
    for line in data:
        temp_length += len(line.decode('utf-8'))
        current_percent = int((temp_length/total_length)*100)
        if current_percent != temp_percent:
            temp_percent = current_percent
            print(str(current_percent) + '%')
        result = re.findall(pattern, line.decode('utf-8'))
        try:
            Parceline.objects.create(ipaddr=result[0][0], dtimefield=datetime.datetime.strptime(result[0][3], '%d/%b/%Y:%H:%M:%S %z'), httpmethod=result[0][4], urlrequest=result[0][5], responsecode=result[0][7], bytesread=result[0][8], referrer=result[0][9], user_agent=result[0][10])
        except Exception:
            Badstring.objects.create(line=line.decode('utf-8'), linenumber=count)
        tmpfile.write(str(line) + '\n')
        count += 1
    print(count)

    def reader(self):
        pass

    def handle(self, *args, **options):
        pass
