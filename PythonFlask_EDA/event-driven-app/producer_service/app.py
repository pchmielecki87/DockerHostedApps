import pika
import json
import time

def send_message():
    connection = pika.BlockingConnection(pika.ConnectionParameters('rabbitmq'))
    channel = connection.channel()

    channel.queue_declare(queue='task_queue', durable=True)

    message = {"event": "Task Created", "description": "A new task has been created."}
    channel.basic_publish(
        exchange='',
        routing_key='task_queue',
        body=json.dumps(message),
        properties=pika.BasicProperties(
            delivery_mode=2,  # make message persistent
        ))
    print(" [x] Sent %r" % message)
    connection.close()

if __name__ == "__main__":
    while True:
        send_message()
        time.sleep(5)  # Send a message every 5 seconds
