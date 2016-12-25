from gui.OutletButton import OutletButton
from scene import *

class OutletManager (Node):
	
	def __init__(self):
		self.showing = False
		self.outlets = []
		
	def add_outlet_button(self, btn):
		btn.alpha = 0
		btn.scale = 1
		self.add_child(btn)
		self.outlets.append(btn)
		btn.position = (self.scene.size.w/2, self.scene.size.h/2 - len(self.outlets)*74 / 2)		
		for i in range(len(self.outlets)):
			y = self.scene.size.h/2 + (len(self.outlets)/2 -0.5 - i)*74
			self.outlets[i].run_action(Action.move_to(self.scene.size.w/2, y, 0.3, TIMING_EASE_OUT))
			
	def show_outlets_for_source(self, src):
		for child in self.outlets:
			child.run_action(Action.fade_to(1.0, 0.3, TIMING_EASE_OUT))
			
	def hide_outlets(self):
		for child in self.outlets:
			if not child.linked > 0:
				child.run_action(Action.fade_to(0.0, 0.3, TIMING_EASE_OUT))	

	def touched(self, touch):
		for child in self.outlets:
			if child.collide(touch):
				return child
		self.hide_outlets()
		return None	
		
		
if __name__ == '__main__':

	class SmartDormApp (Scene):
		def setup(self):
			self.outletManager = OutletManager()
			self.add_child(self.outletManager)
			
			
		def touch_began(self, touch):
			'''out = self.outletManager.touched(touch)
			if out:
				print(out)'''
				
			self.btn = OutletButton('#8fdbe8', SpriteNode('iow:bluetooth_32'))
			self.outletManager.add_outlet_button(self.btn)
			self.outletManager.show_outlets_for_source(None)
			
	run(SmartDormApp(), LANDSCAPE, show_fps=False)
