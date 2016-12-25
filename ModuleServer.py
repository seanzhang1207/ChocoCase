import json
import paho.mqtt.client as mqtt

def on_connect(client, userdata, flags, rc):
	print("Connected with result code "+str(rc))
	client.subscribe("chococase/#")

def on_message(client, userdata, msg):
	print(msg.payload)
	
	data = json.loads(msg.payload.decode())
	
	'''
	PROTOCOL:
	{
	"msg": message type. "module_attach", "module_detach", "module_data"
	"port": port from which the message originated. "A"~"D".
	
	if msg == "module_attach":
	"module": heartrate", "temperature" or "infrared"
	
	elif msg == "module_data":
	"data": data from module
	}
	'''
	if data['msg'] == 'module_attach':
		client.sourceList.add(Source(data['module'], port=data['port']))
		client.sourceList.dirty = True
	elif data['msg'] == 'module_detach':
		client.sourceList.remove(client.sourceList.find_source_at_port(data['port']))
		client.sourceList.dirty = True
	elif data['msg'] == 'module_data':
		src = client.sourceList.find_source_at_port(data['port'])
		for q in src.data:
			q.put(data['data'])
	#print(sourceList.sources)'''
		
from data.Source import Source

def ModuleServer(name, sourceList):
	client = mqtt.Client()
	client.sourceList = sourceList
	client.on_connect = on_connect
	client.on_message = on_message
	print('connecting to server')
	print(client.connect("192.168.1.105", 1883, 60))
	print('connected to server')
	client.loop_forever()

