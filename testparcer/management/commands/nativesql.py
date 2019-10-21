from django.core.management import BaseCommand
from testparcer.models import Parceline,Badstring
from django.db import connection


class Command(BaseCommand):

    def handle(self, *args, **options):
        for p in Badstring.objects.raw('SELECT * from testparcer_badstring WHERE testparcer_badstring.id < 10'):
            print(str(p.id) + '  ' + p.line[:100] + '...    ' + str(p.linenumber))

        # for p in Parceline.objects.raw('SELECT 1 as id, ' +
        #                                 ' Count(testparcer_parceline.ipaddr) AS total,' +
        #                                 'testparcer_parceline.ipaddr,' +
        #                                 "Sum(REGEXP_REPLACE(COALESCE(testparcer_parceline.bytesread, '0'), '[^0-9]*' ,'0')::integer) AS summ " +
        #                                 'FROM ' +
        #                                 'testparcer_parceline ' +
        #                                 'GROUP BY ' +
        #                                 'testparcer_parceline.ipaddr ' +
        #                                 'ORDER BY ' +
        #                                 'summ DESC ' +
        #                                 'LIMIT 10'):
        #     print('\t|' + p.ipaddr + '\t|' + str(p.total) + '\t|' + str(p.summ))

