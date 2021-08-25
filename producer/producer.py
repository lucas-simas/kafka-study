from kafka import KafkaProducer
import json
import random
from time import sleep
from datetime import datetime

# Create an instance of the Kafka producer
producer = KafkaProducer(bootstrap_servers='localhost:9094', value_serializer=lambda v: str(v).encode('utf-8'))

# Call the producer.send method with a producer-record
future = producer.send('meu-topicao', 'Minha msg')
print(future)
result = future.get(timeout=60)
print(result)