from mongoengine import connect
import configparser
import pika


# MongoDB connect
config = configparser.ConfigParser()
config.read("config.ini")


mongo_user = config.get("DB", "user")
mongodb_pass = config.get("DB", "pass")
db_name = config.get("DB", "db_name")
domain = config.get("DB", "domain")

# uri = "mongodb+srv://oivanko:<password>@oivanko.1ehwzwf.mongodb.net/?retryWrites=true&w=majority"
connect(
    host=f"""mongodb+srv://{mongo_user}:{mongodb_pass}@{domain}/{db_name}?retryWrites=true&w=majority""",
    ssl=True,
)


# RabbitMQ connection
credentials = pika.PlainCredentials("guest", "guest")
connection = pika.BlockingConnection(
    pika.ConnectionParameters(host="localhost", port=5672, credentials=credentials)
)
channel = connection.channel()
channel.queue_declare(queue="email_queue")
