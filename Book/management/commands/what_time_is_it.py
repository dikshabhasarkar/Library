from django.core.management.base import BaseCommand
from django.utils import timezone

class Command(BaseCommand):
    help = 'Display Current Time'

    def handle(self,*args,**kwargs):
        time = timezone.now().strftime('%X')
        print(type(time))
        self.stdout.write("It's now %s" %time)

#--o/p--
# >python manage.py what_time_is_it
# <class 'str'>
# It's now 14:01:53