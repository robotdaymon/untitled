import os
from urllib.error import HTTPError

from django.core.management.base import BaseCommand
import urllib.request
import re
import datetime
from testparcer.models import Parceline, Badstring
from untitled.settings import BASE_DIR
from celery import task


class Command(BaseCommand):

    def handle(self, *args, **options):
        print(options['ref'])
        print(type(options['ref']))
        if not options['ref'].endswith("access.log"):
            print('wrong refer to apache log')
            return
        try:
            target_url = options['ref']
        except HTTPError:
            print('Nothing to do here!')
            return
        filename = BASE_DIR + '/parsed-logs/'
        if not os.path.exists(filename):
            os.makedirs(filename)
        filename += str(datetime.datetime.now().strftime('%d-%B-%Y_%H.%M.%S')) + '.log'
        tmpfile = open(str(filename), 'w')
        data = urllib.request.urlopen(target_url)
        pattern = r'(\S+) (\S+) (\S+) \[(.*?)\] \"(\S+) (.*?) (\S+)\" (\S+) (\S+) (\".*\") (\".*?\") (\".*?\")'
        total_length = data.length  # кол-во байт в ответе
        temp_percent = 0  # вычисленный процент временный
        temp_length = 0  # кол-во байт в итерации
        count = 0
        for line in data:
            temp_length += len(line.decode('utf-8'))
            current_percent = int((temp_length / total_length) * 100)
            if current_percent != temp_percent:
                temp_percent = current_percent
                print(str(current_percent) + '%')
            result = re.findall(pattern, line.decode('utf-8'))
            try:
                Parceline.objects.create(ipaddr=result[0][0],
                                         dtimefield=datetime.datetime.strptime(result[0][3], '%d/%b/%Y:%H:%M:%S %z'),
                                         httpmethod=result[0][4], urlrequest=result[0][5], responsecode=result[0][7],
                                         bytesread=result[0][8], referrer=result[0][9], user_agent=result[0][10])
            except Exception:
                Badstring.objects.create(line=line.decode('utf-8'), linenumber=count)
            tmpfile.write(str(line) + '\n')
            count += 1
        print(count)

    def add_arguments(self, parser):
        parser.add_argument("-ref", type=str, required=True)
