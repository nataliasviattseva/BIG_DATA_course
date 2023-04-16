from kafka import KafkaConsumer
import json
import numpy as np

c = KafkaConsumer('test', bootstrap_servers=['localhost:9092'])

def process_msg(msg):
    print(msg.offset)
    print(json.loads(msg.value))

for msg in c:
    process_msg(msg)
from kafka import KafkaConsumer
import json
import numpy as np

c = KafkaConsumer('test', bootstrap_servers=['localhost:9092'])

def process_V(v):
    v1 = v[1:]
    v2 = v[0:-1]
    return(v1-v2)

def process_msg(msg):
    print(msg.offset)
    dico = dict(json.loads(msg.value))
    data = dico['data']
    data1 = np.array(data)
    new_data = process_V(data1)
    print(dico['type'])
    print(new_data)

for msg in c:
    process_msg(msg)