from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
from django.utils.crypto import get_random_string

class Command(BaseCommand):
    help = 'Create random users'

    def add_arguments(self, parser):
        print(parser)
        parser.add_argument('total', type=int, help='Indicates the number of users to be created')
        parser.add_argument('-p', '--prefix', type=str, help='Define a username prefix', )

    def handle(self, *args, **kwargs):
        total = kwargs['total']  # 10
        prefix = kwargs['prefix']  # None
        print(kwargs)
        for i in range(total):  # 10
            if prefix:
                username = '{prefix}_{random_string}'.format(prefix=prefix, random_string=get_random_string(5))  # custom_user_avhhas
            else:
                username = get_random_string(5) #  gjhgj
            User.objects.create_user(username=username, email='', password='123')

# >>> from django.contrib.auth.models import User
# >>> User.objects.all()
# <QuerySet [<User: admin>, <User: AAA>, <User: BBB>, <User: MnDBi>, <User: kf2nD>, <User: LyAKh>, <User: eta3S>, <User: 8HFcL>]>
 
# ----------------------------------------------------
# from django.contrib.auth.models import User
 
#password is not encrypted -not secure password
# User.objects.create(username="AAA",password="admin@123",email="a@gmail.com") 
# <User: AAA>

#encrypted password - secure password
# >>> User.objects.create_user(username="BBB",password="admin@123",email="b@gmail.com")
# <User: BBB>

# dir(User.objects)                          
# ['__class__', '__class_getitem__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', 
# '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__slotnames__', '__str__', '__subclasshook__', '__weakref__', '_constructor_args', '_create_user', '_db', '_get_queryset_methods', '_hints', '_insert', '_queryset_class', '_set_creation_counter', 
# '_update', 'aggregate', 'alias', 'all', 'annotate', 'auto_created', 'bulk_create', 'bulk_update', 'check', 'complex_filter', 'contribute_to_class', 'count', 'create', 'create_superuser', 'create_user', 'creation_counter', 'dates', 'datetimes', 'db', 'db_manager', 'deconstruct', 'defer', 'difference', 'distinct', 'earliest', 'exclude', 'exists', 'explain', 'extra', 'filter', 'first', 'from_queryset', 'get', 'get_by_natural_key', 'get_or_create', 'get_queryset', 'in_bulk', 'intersection', 'iterator', 'last', 'latest', 'make_random_password', 'model', 'name', 'none', 'normalize_email', 'only', 'order_by', 'prefetch_related', 'raw', 'reverse', 'select_for_update', 'select_related', 'union', 'update', 'update_or_create', 'use_in_migrations', 'using', 'values', 'values_list', 'with_perm'] 

