print("Starting consumer...")
from kafka import KafkaConsumer
import json

def calculate_differences(v):
    return [v[i+1]-v[i] for i in range(len(v)-1)]
	
	
#consumer = KafkaConsumer('orders', bootstrap_servers='localhost:9092', value_deserializer=lambda m: json.loads(m.decode('utf-8')))
consumer = KafkaConsumer(
    'orders',
     bootstrap_servers=['localhost:9092'],
     auto_offset_reset='earliest',
     enable_auto_commit=False,
     group_id='my-group',
     value_deserializer=lambda x: loads(x.decode('utf-8')))
for message in consumer:
	print("Received message: ", message)
	print("Received consumer: ", consumer)

	try:
		data = message.value
		V = data['payload']['data']
		V2 = calculate_differences(V)
		result = {'id': data['id'], 'V2': V2}
		print(result)
	except Exception as e:
		print("Error processing message: ", e)