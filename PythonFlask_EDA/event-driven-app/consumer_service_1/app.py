import pika
import json

def callback(ch, method, properties, body):
    message = json.loads(body)
    print(f" [x] Consumer 1 received: {message}")

def consume():
    connection = pika.BlockingConnection(pika.ConnectionParameters('rabbitmq'))
    channel = connection.channel()

    channel.queue_declare(queue='task_queue', durable=True)
    channel.basic_consume(queue='task_queue', on_message_callback=callback, auto_ack=True)

    print(' [*] Consumer 1 Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()

if __name__ == "__main__":
    consume()
