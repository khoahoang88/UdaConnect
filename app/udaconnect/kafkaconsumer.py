from json import loads, dumps
from time import sleep

from kafka import KafkaProducer
from kafka import KafkaConsumer
from kafka.errors import KafkaError



consumer = KafkaConsumer('items', bootstrap_servers=['localhost:9092'],
                            auto_offset_reset = 'earliest',
                            enable_auto_commit = True,
                            value_deserializer = lambda x : x.decode('utf-8')  )

for message in consumer:
    value_message = message.value
    print(value_message)