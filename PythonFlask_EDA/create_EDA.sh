#!/bin/bash

# Create directories
mkdir -p event-driven-app/producer_service
mkdir -p event-driven-app/consumer_service_1
mkdir -p event-driven-app/consumer_service_2

# Create Docker Compose file
cat <<EOL > event-driven-app/docker-compose.yml
version: '3'
services:
  rabbitmq:
    image: 'rabbitmq:3-management'
    ports:
      - '5672:5672'
      - '15672:15672'

  producer_service:
    build: ./producer_service
    depends_on:
      - rabbitmq

  consumer_service_1:
    build: ./consumer_service_1
    depends_on:
      - rabbitmq

  consumer_service_2:
    build: ./consumer_service_2
    depends_on:
      - rabbitmq
EOL

# Producer Service Files
cat <<EOL > event-driven-app/producer_service/app.py
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
EOL

cat <<EOL > event-driven-app/producer_service/Dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["python", "app.py"]
EOL

echo "pika==1.2.0" > event-driven-app/producer_service/requirements.txt

# Consumer Service 1 Files
cat <<EOL > event-driven-app/consumer_service_1/app.py
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
EOL

cat <<EOL > event-driven-app/consumer_service_1/Dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["python", "app.py"]
EOL

echo "pika==1.2.0" > event-driven-app/consumer_service_1/requirements.txt

# Consumer Service 2 Files
cat <<EOL > event-driven-app/consumer_service_2/app.py
import pika
import json

def callback(ch, method, properties, body):
    message = json.loads(body)
    print(f" [x] Consumer 2 received and processed: {message}")

def consume():
    connection = pika.BlockingConnection(pika.ConnectionParameters('rabbitmq'))
    channel = connection.channel()

    channel.queue_declare(queue='task_queue', durable=True)
    channel.basic_consume(queue='task_queue', on_message_callback=callback, auto_ack=True)

    print(' [*] Consumer 2 Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()

if __name__ == "__main__":
    consume()
EOL

cat <<EOL > event-driven-app/consumer_service_2/Dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["python", "app.py"]
EOL

echo "pika==1.2.0" > event-driven-app/consumer_service
