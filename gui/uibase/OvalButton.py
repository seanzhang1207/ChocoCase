from scene import *


class OvalButton (ShapeNode):

	def __init__(self, color, icon):
		self.background = ui.Path.oval(0, 0, 56, 56)
		self.background.line_width = 0
		shadow = ('#80000000', 2, 2, 5)
		super(OvalButton, self).__init__(self.background, color, 'silver', shadow=shadow)
		icon.scale = 1.2
		icon.position = (-2, 2)
		self.add_child(icon)
		self.selected = False

	def collide(self, touch):
		x = self.point_from_scene(touch.location).x
		y = self.point_from_scene(touch.location).y
		if x ** 2 + y ** 2 <= 28**2:
			return True
		else:
			return False
			
	def select(self):
		self.background.line_width = 2
		
	def deselect(self):
		self.background.line_width = 0
		
		
if __name__ == '__main__':

	class SmartDormApp (Scene):
		def setup(self):
			self.background_color = '#203040'
			self.btn = OvalButton('#8fdbe8', SpriteNode('iow:bluetooth_32'))
			self.btn.position = (70, 130)
			
			self.add_child(self.btn)
			
			
		def touch_began(self, touch):
			if self.btn.collide(touch):
				print(self.btn.path.line_width)
			
	run(SmartDormApp(), PORTRAIT, show_fps=False)
