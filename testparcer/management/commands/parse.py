from django.core.management.base import BaseCommand
import urllib.request
import re


class Command(BaseCommand):
    target_url = 'http://www.almhuette-raith.at/apache-log/access.log'
    data = urllib.request.urlopen(target_url)
    pattern = r'(\S+) (\S+) (\S+) \[(.*?)\] \"(\S+) (.*?) (\S+)\" (\S+) (\S+) (\".*?\") (\".*?\")'
    count = 0
    for line in data:
        count += 1
        if count % 1000 == 0:
            print(count)
            result = re.findall(pattern, str(line))
            print(result)
    print(count)

    def reader(self):
        pass

    def handle(self, *args, **options):
        pass
