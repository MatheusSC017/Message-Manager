import pika
import json
import logging
from utils.messages import send_whatsapp_message, send_email


logging.basicConfig(
    filename='message.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)


def email_callback(ch, method, properties, body):
    logger = logging.getLogger(__name__)

    message = json.loads(body)
    if message['subject'] in ['appointment', 'devolution', 'late devolution', 'invoice']:
        send_email(**message)
        logger.info(message)
        print("Message Sent!")

    ch.basic_ack(delivery_tag=method.delivery_tag)


def whatsapp_callback(ch, method, properties, body):
    message = json.loads(body)
    send_whatsapp_message(message['recipient'], message['content'])
    ch.basic_ack(delivery_tag=method.delivery_tag)


def consumer(name, queue, callback):
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()

    channel.queue_declare(queue=queue)
    channel.basic_consume(queue=queue, on_message_callback=callback)
    print(f'{name.title()} Consumer waiting for messages. To exit press CTRL+C')
    channel.start_consuming()

