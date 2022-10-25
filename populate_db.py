import os, django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'setup.settings')
django.setup()

from faker import Faker
import random
from clients.models import Client

def create_people(quantity):
    fake = Faker('en_US')
    Faker.seed(10)
    for _ in range(quantity):
        name = fake.name()
        email = '{}@{}'.format(name.lower(), fake.free_email_domain())
        email = email.replace(' ', '')
        ssn = fake.ssn()
        phone = f'{random.randrange(100,999)}-{random.randrange(100,999)}-{random.randrange(1000,9999)}'
        active = random.choice([True, False])
        p = Client(name=name, email=email, ssn=ssn, phone=phone, active=active)
        p.save()

create_people(50)