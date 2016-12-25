from scene import *
from gui.uibase.RoundRectButton import RoundRectButton

class SourceButton (RoundRectButton):
	def __init__(self, source):
		self.linked = 0
		self.source = source
		super(SourceButton, self).__init__(self.source.color, self.source.icon)

