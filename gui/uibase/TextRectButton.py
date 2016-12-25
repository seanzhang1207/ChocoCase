from scene import *


class TextRectButton (ShapeNode):

	def __init__(self, color, text):
		self.text = text
		self.background = ui.Path.rounded_rect(0, 0, 60, 60, 10)
		self.background.line_width = 0
		shadow = ('#80000000', 1, 1, 2)
		super(TextRectButton, self).__init__(self.background, color, 'silver', shadow=shadow)
		if len(text) == 1:
			buttontext = LabelNode(text, font=('helvetica', 30), color='#e8dfdf')
		else:
			buttontext = LabelNode(text, font=('helvetica', 20), color='#e8dfdf')
		
		self.add_child(buttontext)
		self.selected = False

	def collide(self, touch):
		x = self.point_from_scene(touch.location).x
		y = self.point_from_scene(touch.location).y
		if x > -30 and x < 30 and y > -30 and y < 30:
			return True
		else:
			return False

		
		
		
if __name__ == '__main__':

	class SmartDormApp (Scene):
		def setup(self):
			self.btn = TextRectButton('#5277d5', '1')
			self.btn.position = (100, 100)
			self.add_child(self.btn)
		
			
	run(SmartDormApp(), PORTRAIT, show_fps=False)
