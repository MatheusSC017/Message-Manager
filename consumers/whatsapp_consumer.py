import pika
from consumer import whatsapp_callback

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.queue_declare(queue='whatsapp_queue')
channel.basic_consume(queue='whatsapp_queue', on_message_callback=whatsapp_callback)
print('WhatsApp Consumer waiting for messages. To exit press CTRL+C')
channel.start_consuming()
