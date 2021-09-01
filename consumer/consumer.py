from kafka import KafkaConsumer

consumer = KafkaConsumer('meutopicao', bootstrap_servers='localhost:9094')

for msg in consumer:
    print (msg)


# # consume earliest available messages, don't commit offsets
# KafkaConsumer(auto_offset_reset='earliest', enable_auto_commit=False)

# # consume json messages
# KafkaConsumer(value_deserializer=lambda m: json.loads(m.decode('ascii')))

# # consume msgpack
# KafkaConsumer(value_deserializer=msgpack.unpackb)

# # StopIteration if no message after 1sec
# KafkaConsumer(consumer_timeout_ms=1000)

# # Subscribe to a regex topic pattern
# consumer = KafkaConsumer()
# consumer.subscribe(pattern='^awesome.*')

# # Use multiple consumers in parallel w/ 0.9 kafka brokers
# # typically you would run each on a different server / process / CPU
# consumer1 = KafkaConsumer('kafka-python-topic', bootstrap_servers=['localhost:9092'])
# consumer2 = KafkaConsumer('kafka-python-topic', bootstrap_servers=['localhost:9092'])