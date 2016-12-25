from scene import *
from gui.uibase.OvalButton import OvalButton

class OutletButton (OvalButton):
	def __init__(self, outlet):
		self.linked = 0
		self.outlet = outlet
		super(OutletButton, self).__init__(outlet.color, outlet.icon)


