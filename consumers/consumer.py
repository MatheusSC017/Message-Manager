import pika
import json
from utils.messages import send_whatsapp_message, send_email


def email_callback(ch, method, properties, body):
    message = json.loads(body)
    send_email(message['recipient'], message['content'])
    ch.basic_ack(delivery_tag=method.delivery_tag)


def whatsapp_callback(ch, method, properties, body):
    message = json.loads(body)
    send_whatsapp_message(message['recipient'], message['content'])
    ch.basic_ack(delivery_tag=method.delivery_tag)


def consumer(queue):
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()

    channel.queue_declare(queue=queue)
    channel.basic_consume(queue=queue, on_message_callback=callback)
    print('WhatsApp Consumer waiting for messages. To exit press CTRL+C')
    channel.start_consuming()

