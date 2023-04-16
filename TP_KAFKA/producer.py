import json
import numpy
import time

from kafka import KafkaProducer

producer = KafkaProducer(bootstrap_servers='localhost:9092')
i = 0
while True:
	i += 1
	data = {'id' : i, 'payload' : {'data': list(numpy.random.standard_normal(100))}}
	producer.send('orders', json.dumps(data).encode('utf-8'))
	producer.flush()
	time.sleep(1)
	