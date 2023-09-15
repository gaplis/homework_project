from random import randint

from django.core.management import BaseCommand


from homework_2_app.models import Client


class Command(BaseCommand):
    help = 'Generate fake clients'

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='Count clients')

    def handle(self, *args, **kwargs):
        count = kwargs.get('count')
        for i in range(1, count + 1):
            client = Client(name=f'Name{i}',
                            email=f'mail{i}@mail.ru',
                            phone=f'8-{randint(900, 999)}-{randint(100, 999)}-{randint(10, 99)}-{randint(10, 99)}',
                            address=f'Address{i}')
            client.save()

