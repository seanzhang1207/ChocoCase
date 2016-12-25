from scene import *
from gui.uibase.RoundRectButton import RoundRectButton

class DestinationButton (RoundRectButton):
	def __init__(self, destination):
		self.destination = destination
		self.linked = 0
		super(DestinationButton, self).__init__(self.destination.color, self.destination.icon)
