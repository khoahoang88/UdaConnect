from json import loads, dumps
from time import sleep

from kafka import KafkaProducer
from kafka import KafkaConsumer
from kafka.errors import KafkaError



producer = KafkaProducer(bootstrap_servers=['localhost:9092'], value_serializer = lambda x:dumps(x).encode('utf-8') )

for n in range(500):
    my_data = {'num' : n}
    producer.send('items', value = my_data)
    sleep(1)




