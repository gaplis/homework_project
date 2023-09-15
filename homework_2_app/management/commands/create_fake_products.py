from random import uniform, randint

from django.core.management import BaseCommand

from homework_2_app.models import Product


class Command(BaseCommand):
    help = 'Generate fake products'

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='Count products')

    def handle(self, *args, **kwargs):
        count = kwargs.get('count')
        for i in range(1, count + 1):
            product = Product(name=f'Name{i}',
                              description=f'Description{i}',
                              price=f'{round(uniform(100, 3000), 2)}',
                              count=f'{randint(100, 100000)}', )
            product.save()
