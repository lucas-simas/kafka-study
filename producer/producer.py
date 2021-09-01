from kafka import KafkaProducer
import json
import random
from time import sleep
from datetime import datetime

# Create an instance of the Kafka producer
producer = KafkaProducer(bootstrap_servers='localhost:9094', value_serializer=lambda v: str(v).encode('utf-8'))

print(producer.send('meutopicao', b'121221dsads').get(timeout=30))
producer.flush()