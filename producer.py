from faker import Faker
from connection_mongodb import connect
from contact_model import Contact
import json
from connection_rabbit import connection, channel


num_of_contacts = 15
fake = Faker()


for _ in range(num_of_contacts):
    new_contact = Contact(full_name=fake.name(), email=fake.email())
    new_contact.save()

    # відправлення повідлмлення до чергм
    message = {"contact_id": str(new_contact.id)}
    channel.basic_publish(
        exchange="", routing_key="email_queue", body=json.dumps(message)
    )

print(f"{num_of_contacts} are created and added to the queue")
connection.close()
