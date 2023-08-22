import pika

import json

from db.create_contacts import create_contacts
from db.models import Contacts
from db.connect_db import connect

credentials = pika.PlainCredentials("guest", "guest")
connection = pika.BlockingConnection(
    pika.ConnectionParameters(host="localhost", port=5672, credentials=credentials)
)
channel = connection.channel()

channel.exchange_declare(exchange="hw8", exchange_type="direct")
channel.queue_declare(queue="contacts", durable=True)
channel.queue_bind(exchange="hw8", queue="contacts")


def main(number_contacts: int = 15):
    create_contacts(number_contacts)
    contacts = Contacts.objects()
    for contact in contacts:
        message = {
            "payload": f"{contact.id}",
        }

        channel.basic_publish(
            exchange="hw8",
            routing_key="contacts",
            body=json.dumps(message).encode(),
            properties=pika.BasicProperties(
                delivery_mode=pika.spec.PERSISTENT_DELIVERY_MODE
            ),
        )
        print(" [x] Sent %r" % message)
    connection.close()


if __name__ == "__main__":
    main()
