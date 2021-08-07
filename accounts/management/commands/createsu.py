from django.core.management.base import BaseCommand

from accounts.models import User


class Command(BaseCommand):
    help = 'Creates Organization for Django Tenant'

    def handle(self, *args, **kwargs):
        if not User.objects.filter(email='zackcpetersen@gmail.com').first():
            User.objects.create_superuser(
                email='zackcpetersen@gmail.com', first_name='Zack', last_name='Petersen', password='admin')
            self.stdout.write(self.style.SUCCESS(
                'Successfully created superuser for zackcpetersen@gmail.com'))
