from gui.AddDestinationButton import AddDestinationButton
from gui.DestinationButton import DestinationButton

from scene import *

class DestinationManager (Node):
	
	def __init__(self):
		self.showing = False
		self.addButton = AddDestinationButton()
		self.addButton.alpha = 0
		self.add_child(self.addButton)
		self.destinations = []
		self.ipWindow = None
		self.inputing = False
		
	def add_destination_button(self, btn):
		btn.alpha = 0
		btn.scale = 1
		self.add_child(btn)
		self.destinations.append(btn)
		btn.position = (self.scene.size.w-50, self.scene.size.h/2 - len(self.destinations)*80 / 2)		
		self.addButton.run_action(Action.move_to(self.scene.size.w-50, self.scene.size.h/2 - ((len(self.destinations)+1)/2 - 0.5)*80, 0.3, TIMING_EASE_OUT))
		for i in range(len(self.destinations)):
			y = self.scene.size.h/2 + (len(self.destinations)/2 -1 - i+1)*80
			self.destinations[i].run_action(Action.move_to(self.scene.size.w-50, y, 0.3, TIMING_EASE_OUT))
			
	def show_destinations_for_outlet(self, out):
		self.addButton.run_action(Action.move_to(self.scene.size.w-50, self.scene.size.h/2 - ((len(self.destinations)+1)/2 - 0.5)*80, 0.3, TIMING_EASE_OUT))
		self.addButton.run_action(Action.fade_to(1.0, 0.3, TIMING_EASE_OUT))
		for child in self.destinations:
			child.run_action(Action.fade_to(1.0, 0.3, TIMING_EASE_OUT))
			
	def hide_destinations(self):
		self.addButton.run_action(Action.fade_to(0, 0.3, TIMING_EASE_OUT))
		for child in self.destinations:
			if not child.linked > 0:
				child.run_action(Action.fade_to(0.0, 0.3, TIMING_EASE_OUT))

	def touched(self, touch):
		for child in self.destinations:
			if child.collide(touch):
				return child
		if self.addButton.collide(touch):
			return 'input'
		
		
if __name__ == '__main__':

	class SmartDormApp (Scene):
		def setup(self):
			self.DestinationManager = DestinationManager()
			self.add_child(self.DestinationManager)
			
			
		def touch_began(self, touch):
			'''out = self.outletManager.touched(touch)
			if out:
				print(out)'''
				
			self.btn = DestinationButton('#adecd1', SpriteNode('iow:icon_social_google_plus_32'))
			self.DestinationManager.add_destination_button(self.btn)
			self.DestinationManager.show_destinations_for_outlet(None)
			
	run(SmartDormApp(), LANDSCAPE, show_fps=False)
