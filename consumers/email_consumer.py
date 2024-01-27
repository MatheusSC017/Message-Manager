import pika
from consumer import email_callback

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.queue_declare(queue='email_queue')
channel.basic_consume(queue='email_queue', on_message_callback=email_callback)
print('Email Consumer waiting for messages. To exit press CTRL+C')
channel.start_consuming()
