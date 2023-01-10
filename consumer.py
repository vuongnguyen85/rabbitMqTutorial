import pika, sys, os


def main():
    connection_parameters = pika.ConnectionParameters(host='localhost')
    connection = pika.BlockingConnection(connection_parameters)
    channel = connection.channel()  # create channel

    channel.queue_declare(queue='letterbox')  # declare queue

    def on_message_received(ch, method, properties, body):
        print(f"Received new message: {body}")

    channel.basic_consume(queue='letterbox', on_message_callback=on_message_received, auto_ack=True)  # auto_ack = automatically acknowledge the message

    print('Started consuming...')
    channel.start_consuming()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('\nInterrupted, closing consumer')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
