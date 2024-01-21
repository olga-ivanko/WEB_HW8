import json
from connection import connect, channel, connection
from models import Contact


# stub function:
def send_email(contact):
    name = contact["full_name"]
    email = contact["email"]
    print(f"Mail to {name} on email:{email}")
    contact.is_sent = True
    contact.save()


def callback(ch, method, properties, body):
    message = json.loads(body.decode())
    contact_id = message["contact_id"]

    contact = Contact.objects.get(id=contact_id)

    send_email(contact)
    name = contact["full_name"]

    print(f"The message for {name} is processed.")
    ch.basic_ack(delivery_tag=method.delivery_tag)


channel.basic_consume(queue="email_queue", on_message_callback=callback)
print("Waiting for message. Print CTRL+C for exit")
channel.start_consuming()
