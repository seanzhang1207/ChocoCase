from scene import *


class LongTextRectButton (ShapeNode):

	def __init__(self, color, text):
		self.background = ui.Path.rounded_rect(0, 0, 60, 130, 10)
		self.background.line_width = 0
		shadow = ('#80000000', 2, 2, 5)
		super(LongTextRectButton, self).__init__(self.background, color, 'silver', shadow=shadow)
		buttontext = LabelNode(text, font=('helvetica', 30), color='#e8dfdf')
		buttontext.position = (-2, 2)
		self.add_child(buttontext)
		self.selected = False

	def collide(self, touch):
		x = self.point_from_scene(touch.location).x
		y = self.point_from_scene(touch.location).y
		if x > -30 and x < 30 and y > -65 and y < 65:
			return True
		else:
			return False
