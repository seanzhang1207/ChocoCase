from queue import Queue
from threading import Thread
import socket
import location
import motion
import time
from objc_util import *

def ModuleSource(name, inq, outqs):
	while True:
		data = inq.get()
		for q in outqs:
			sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			sock.sendto(str(data).encode(), dest)

def ModuleJob(name, q, dest):
	while True:
		data = q.get()
		sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		sock.sendto(str(data).encode(), dest)
		

def GpsSource(name, q):
	while True:
		location.start_updates()
		q.put(location.get_location())
		location.stop_updates()
		time.sleep(5)

def GpsJob(name, q, dest):
	while True:
		print('gps send')
		data = q.get()
		sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		sock.sendto(str(data).encode(), dest)
		


def MotionSource(name, q):
	motion.start_updates()
	while True:
		q.put(motion.get_user_acceleration())
		time.sleep(0.05)
		
def MotionJob(name, q, dest):
	while True:
		data = q.get()
		sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		sock.sendto(str(data).encode(), dest)
		

def AmbientLightSource(name, q):
	UIDevice = ObjCClass('UIDevice')
	d = UIDevice.new()
	while True:
		q.put(d._backlightLevel())
		time.sleep(3)
		
def AmbientLightJob(name, q, dest):
	while True:
		data = q.get()
		sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		sock.sendto(str(data).encode(), dest)

def JobServer(name, linkList):
	hasSource = {}
	while True:
		for link in linkList:
			if not link.running:
				link.running = True
				src = link.src.source
				out = link.out.outlet
				print(src.type, out.type)
				if src.type in ['heartrate', 'infrared', 'temperature']:
					q = Queue()
					src.data.append(q)
					job = Thread(target=ModuleJob, args=(src.type, q, link.dest.destination.addr))
					job.start()
				
				elif src.type == 'gyro':
					dataqueue = Queue()
					generator = Thread(target=MotionSource, args=('motionsrc', dataqueue))
					job = Thread(target=MotionJob, args=('motion', dataqueue, link.dest.destination.addr))
					generator.start()
					job.start()
				elif src.type == 'gps':
					dataqueue = Queue()
					generator = Thread(target=GpsSource, args=('gpssrc', dataqueue))
					job = Thread(target=GpsJob, args=('gps', dataqueue, link.dest.destination.addr))
					generator.start()
					job.start()
				elif src.type == 'ambientlight':
					dataqueue = Queue()
					generator = Thread(target=AmbientLightSource, args=('ambientlightsrc', dataqueue))
					job = Thread(target=AmbientLightJob, args=('ambientlight', dataqueue, link.dest.destination.addr))
					generator.start()
					job.start()
				

				
				
