from django.core.management import BaseCommand
from homework_2_app.models import Client


class Command(BaseCommand):
    help = 'Delete client by ID'

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='ID client')

    def handle(self, *args, **kwargs):
        pk = kwargs.get('pk')
        client = Client.objects.filter(pk=pk).first()
        client.delete()

        self.stdout.write(f'Удалили клиента: {client}')
