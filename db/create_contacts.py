from db.models import Contacts
from db.connect_db import connect

import faker

fake_data = faker.Faker("en_GB")


def create_contacts(number_contacts: int = 10):
    Contacts.objects.delete()
    for _ in range(number_contacts):
        fullname = fake_data.name()
        Contacts(
            fullname=fullname,
            email=f'{fullname.split(" ")[-2].lower()}.{fullname.split(" ")[-1].lower()}@{fake_data.free_email_domain()}',
        ).save()


if __name__ == "__main__":
    create_contacts()
