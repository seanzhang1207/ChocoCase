from scene import *
from queue import Queue

class Source (object):
	def __init__(self, src_type, port=None, ip=None, devid=None, side=None):
		self.dirty = True
		self.type = src_type
		self.module = False
		if self.type == 'wifi':
			self.icon = SpriteNode('iow:wifi_32')
			self.color = "#c7b7eb"
			self.ip = ip
			self.category == 'wifi'
		elif self.type == 'bluetooth':
			self.icon = SpriteNode('iow:bluetooth_32')
			self.color = "#82c2ea"
			self.devid = devid
			self.category = 'bluetooth'
		elif self.type == 'microphone':
			self.icon = SpriteNode('iow:ios7_mic_32')
			self.color = "#d47adc"
			self.category = 'microphone'
		elif self.type == 'camera':
			self.icon = SpriteNode('iow:camera_32')
			self.color = "#b282ea"
			self.side = camside
			self.category = 'camera'
		else:
			self.data = []
			if self.type == 'ambientlight':
				self.color = '#f2d36c'
				self.icon = SpriteNode('iow:ios7_lightbulb_32')
				self.category = 'phone'
			elif self.type == 'gps':
				self.color = '#a2aff3'
				self.icon = SpriteNode('iow:earth_32')
				self.category = 'phone'
			elif self.type == 'gyro':
				self.color = '#eab282'
				self.icon = SpriteNode('typw:Line_Chart')
				self.category = 'phone'
			elif self.type == 'infrared':
				self.color = '#ea6890'
				self.icon = SpriteNode('iow:radio_waves_32')
				self.port = port
				self.module = True
				self.category = 'module'
			elif self.type == 'temperature':
				self.color = '#ffa355'
				self.icon = SpriteNode('iow:thermometer_32')
				self.port = port
				self.module = True
				self.category = 'module'
			elif self.type == 'heartrate':
				self.color = "#ff6f55"
				self.icon = SpriteNode('iow:heart_32')
				self.port = port
				self.module = True
				self.category = 'module'
