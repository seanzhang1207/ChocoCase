from scene import *

class Destination (object):
	def __init__(self, type, addr=None, devid=None):
		self.type = type
		if type == 'wifi':
			self.addr = addr
			self.color = '#62aee8'
			self.icon = LabelNode(self.addr[0] + ':' + str(self.addr[1]), font=('helvetica', 7))
		elif type == 'bluetooth':
			self.devid = 0

