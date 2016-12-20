from scene import *


class RoundRectButton (ShapeNode):

	def __init__(self, color, icon):
		background = ui.Path.rounded_rect(0, 0, 70, 70, 10)
		background.line_width = 0
		shadow = ('#80000000', 2, 2, 5)
		super(RoundRectButton, self).__init__(background, color, 'silver', shadow=shadow)
		icon.scale = 1.5
		self.add_child(icon)

	def collide(self, touch):
		x = touch.location.x
		y = touch.location.y
		if x > self.position.x - 35 and x < self.position.x + 35 and y > self.position.y - 35 and y < self.position.y + 35:
			return True
		else:
			return False
