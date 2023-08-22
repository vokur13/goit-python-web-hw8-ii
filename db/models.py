from datetime import datetime

from mongoengine import Document, StringField, DateTimeField, BooleanField


class Contacts(Document):
    fullname = StringField(required=True, max_length=255)
    email = StringField(required=True, max_length=255, unique=True)
    is_sent = BooleanField(required=True, default=False)
    created_at = DateTimeField(default=datetime.now())
