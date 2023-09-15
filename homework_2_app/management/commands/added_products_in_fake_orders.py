from random import uniform, randint

from django.core.management import BaseCommand

from homework_2_app.models import Order, Product


class Command(BaseCommand):
    help = 'Added products in fake orders'

    def handle(self, *args, **kwargs):
        for o in Order.objects.all():
            for i in range(3):
                pk = randint(1, len([p for p in Product.objects.all()]) - 1)
                p = Product.objects.filter(pk=pk).first()
                o.products.add(p)
                o.total_price += p.price
                o.save()
