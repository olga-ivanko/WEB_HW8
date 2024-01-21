from mongoengine import Document, StringField, BooleanField, ListField, ReferenceField


class Author(Document):
    fullname = StringField(reqiired=True)
    born_date = StringField(required=True)
    born_location = StringField(required=True)
    description = StringField(required=True)


class Quote(Document):
    tags = ListField(StringField())
    author = ReferenceField(Author)
    quote = StringField(required=True)


class Contact(Document):
    full_name = StringField(required=True)
    email = StringField(required=True)
    is_sent = BooleanField(default=False)
