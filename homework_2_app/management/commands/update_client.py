from django.core.management import BaseCommand
from homework_2_app.models import Client


class Command(BaseCommand):
    help = 'Update client name by ID'

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='ID client')
        parser.add_argument('name', type=str, help='Name client')

    def handle(self, *args, **kwargs):
        pk = kwargs.get('pk')
        name = kwargs.get('name')
        client = Client.objects.filter(pk=pk).first()
        client.name = name
        client.save()

        self.stdout.write(f'Обновили имя о клиента: {client}')
