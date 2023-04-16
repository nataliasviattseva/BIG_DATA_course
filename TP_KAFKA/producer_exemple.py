from kafka import KafkaProducer
import json
import numpy as np
import time

p = KafkaProducer(bootstrap_servers=['localhost:9092'])

i = 0
while True:
    v = np.random.uniform(0, 2, 100)
    data1 = str(v.tolist())
    data2 = eval(data1)
    data = { 'id': i,
        'type': 'uni',
        'data': data2}

    p.send('test', json.dumps(data).encode('utf-8'))
    p.flush()

    i += 1
    time.sleep(2)