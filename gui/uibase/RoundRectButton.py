from scene import *


class RoundRectButton (ShapeNode):

	def __init__(self, color, icon):
		self.background = ui.Path.rounded_rect(0, 0, 70, 70, 10)
		self.background.line_width = 0
		shadow = ('#80000000', 2, 2, 5)
		super(RoundRectButton, self).__init__(self.background, color, 'silver', shadow=shadow)
		icon.scale = 1.2
		icon.position = (-2, 2)
		self.add_child(icon)
		self.selected = False

	def collide(self, touch):
		x = self.point_from_scene(touch.location).x
		y = self.point_from_scene(touch.location).y
		if x > -35 and x < 35 and y > -35 and y < 35:
			return True
		else:
			return False
			
	def select(self):
		self.path.line_width = 2
		
	def deselect(self):
		self.path.line_width = 0
