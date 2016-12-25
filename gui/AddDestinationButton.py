from scene import *
from gui.uibase.OvalButton import OvalButton

class AddDestinationButton (OvalButton):
	def __init__(self):
		super(AddDestinationButton, self).__init__('#ff6c6c', SpriteNode('iow:plus_32'))
