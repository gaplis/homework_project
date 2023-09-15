from random import uniform, randint

from django.core.management import BaseCommand

from homework_2_app.models import Order, Client


class Command(BaseCommand):
    help = 'Generate fake orders'

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='Count orders')

    def handle(self, *args, **kwargs):
        count = kwargs.get('count')
        for i in range(1, count + 1):
            order = Order(customer=Client.objects.all()[i - 1])
            order.save()
