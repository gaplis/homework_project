from django.core.management import BaseCommand
from homework_2_app.models import Client


class Command(BaseCommand):
    help = 'Read clients'

    def handle(self, *args, **kwargs):
        clients = Client.objects.all()
        for client in clients:
            self.stdout.write(f'{client}')
