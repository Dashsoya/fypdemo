from django.db import connection
from django.core.management.base import BaseCommand
from django.core.management import call_command
from demo.models import CustomUser
import random

class Command(BaseCommand):
    help = 'Reset the database by dropping all tables and recreating them'

    def handle(self, *args, **options):
        # Delete all rows from the custom user table
        CustomUser.objects.all().delete()

        # Reset the auto-increment sequence for the account_id field
        with connection.cursor() as cursor:
            cursor.execute("DELETE FROM sqlite_sequence WHERE name='demo_customuser'")

        newUser, created = CustomUser.objects.get_or_create(username='admin1', email='admin1@gmail.com', role='admin', status='normal', phone_number='33333333', name='admin1')
        newUser.set_password('admin1')
        newUser.save()

         # Generate new users
        for i in range(10):
            role = random.choice(['patient', 'doctor'])
            status = 'not_applicable' if role == 'doctor' else random.choice(['covid', 'normal'])
            
            username = f'{role}{i+1}'
            email = f'{username}@gmail.com'
            phone_number = ''.join(random.choices('0123456789', k=8))  # Generate a random phone number
            name = f'User {i+1}'

            # Create a new user
            newUser, created = CustomUser.objects.get_or_create(
                username=username,
                email=email,
                role=role,
                status=status,
                phone_number=phone_number,
                name=name
            )
            
            # Set the password for the new user
            newUser.set_password(username)
            newUser.save()


        # Apply migrations
        call_command('migrate')

        self.stdout.write(self.style.SUCCESS('Database reset completed successfully!'))
