from django.contrib.auth.models import User
from django.core.management.base import BaseCommand

class Command(BaseCommand):

    help = "Creates an admin user non-interactively if no admin users exist"

    def add_arguments(self, parser):
        parser.add_argument('--username', help="Admin's username")
        parser.add_argument('--email', help="Admin's email")
        parser.add_argument('--password', help="Admin's password")

    def handle(self, *args, **options):
        if User.objects.filter(is_superuser=True).count() == 0:
            User.objects.create_superuser(username=options['username'],
                                          email=options['email'],
                                          password=options['password'])
