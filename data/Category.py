from scene import *

class Category (object):
	
	def __init__(self, category):
		self.name = category
		if self.name == 'wifi':
			self.color = '#53c6d9'
			self.icon = SpriteNode('iow:wifi_32')
		elif self.name == 'bluetooth':
			self.color = '#537ad9'
			self.icon = SpriteNode('iow:bluetooth_32')
		elif self.name == 'microphone':
			self.icon = SpriteNode('iow:ios7_mic_32')
			self.color = "#d47adc"
		elif self.name == 'camera':
			self.icon = SpriteNode('iow:camera_32')
			self.color = "#b282ea"
		elif self.name == 'sensor':
			self.icon = SpriteNode('iow:radio_waves_32')
			self.color = "#8ad76b"
		elif self.name == 'phone':
			self.color = '#6ab7c4'
			self.icon = SpriteNode('iow:iphone_32')
		elif self.name == 'module':
			self.color = '#96bf60'
			self.icon = SpriteNode('iow:more_32')
