RabbitMQ Tutorial (Python)
===============

This can be use to set up a consumer (listen and consumes message) and a producer (sends a message to queue). 

## Running Instructions
1. First, we need to start Docker and running the following: 

```
docker run -it --rm --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:3.11-management
```
This will run RabbitMQ on our local machine.

2. To start consumer, we just run the following:
```
python3 consumer.py
```

3. On another terminal window, we run the following to start producer which will send a message to our queue:
```
python3 producer.py
```
Note: we can run this multiple times to send multiple messages. If we follow steps in this order, as consumer is also running, message will be consumed straight away. 
We can also not start consumer and then messages will just build up on our queue.