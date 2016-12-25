from scene import *

class Outlet (object):
	def __init__(self, outtype):
		self.type = outtype
		if self.type == 'wifi':
			self.color = '#537ad9'
			self.icon = SpriteNode('iow:wifi_32')
			self.need_destination = True
		elif self.type == 'infrared':
			self.color = '#ea6890'
			self.icon = SpriteNode('iow:radio_waves_32')
			self.need_destination = False
		elif self.type == 'bluetooth':
			self.icon = SpriteNode('iow:bluetooth_32')
			self.color = "#82c2ea"
			self.need_destination = True
