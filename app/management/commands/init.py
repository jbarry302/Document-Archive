import random
from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
from django.utils import timezone
from faker import Faker
from app.models import Document

fake = Faker()

class Command(BaseCommand):
    help = 'Populates the Document model with fake data'

    def create_superuser(self):
        if not User.objects.filter(is_superuser=True).exists():
            self.stdout.write(self.style.SUCCESS('Creating superuser...'))
            User.objects.create_superuser(
                username='admin',
                email='admin@yahoo.com',
                password='pass'
            )
            self.stdout.write(self.style.SUCCESS('Superuser created successfully!'))
        else:
            self.stdout.write(self.style.SUCCESS('Superuser already exists!'))

    def create_documents(self, n=20):
        self.stdout.write(self.style.SUCCESS('Creating fake documents...'))
        for _ in range(n):
            title = fake.text(max_nb_chars=50)
            description = fake.paragraph()
            file_document = None
            document_url = fake.url() if random.choice([True, False]) else None
            picture = None
            note = fake.text()

            Document.objects.create(
                title=title,
                description=description,
                file_document=file_document,
                document_url=document_url,
                picture=picture,
                note=note
            )

        self.stdout.write(self.style.SUCCESS('Fake documents created successfully!'))

    def handle(self, *args, **options):
        self.create_superuser()
        # self.create_documents()

