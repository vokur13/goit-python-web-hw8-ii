from db.models import Contacts
from db.connect_db import connect
from utilities.email_handler import email_handler

contact_id = "64e335a318dd7bf5c6698d7c"


def update_contact(object_id):
    contact = Contacts.objects(id=object_id)

    for c in contact:
        email_handler(c.email)

    contact.update(is_sent=True)

    contact = Contacts.objects(id=object_id)

    for c in contact:
        print(c.to_mongo().to_dict())


if __name__ == "__main__":
    update_contact(contact_id)
