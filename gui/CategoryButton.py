from scene import *
from gui.uibase.RoundRectButton import RoundRectButton
from gui.SourceButton import SourceButton

class CategoryButton (RoundRectButton):
	def __init__(self, category):
		self.category = category
		self.source_buttons = []
		self.showing = False
		super(CategoryButton, self).__init__(self.category.color, self.category.icon)
		
	def hide_sources(self):
		self.showing = False
		for child in self.source_buttons:
			child.run_action(Action.group(Action.fade_to(0, 0.3, TIMING_EASE_OUT), Action.move_to(0, 0, 0.3, TIMING_EASE_OUT)))
			
	def show_sources(self):
		self.showing = True
		for i in range(len(self.source_buttons)):
			child = self.source_buttons[i]
			x = 90
			y = (len(self.source_buttons)/2.0 - 0.5 - i) * 80
			child.run_action(Action.group(Action.fade_to(1.0, 0.3, TIMING_EASE_OUT), Action.move_to(x, y, 0.3, TIMING_EASE_OUT)))
		
	def touched(self, touch):
		self.showing = not self.showing
		if self.showing:
			self.show_sources()
		else:
			for child in self.source_buttons:
				if child.collide(touch):
					#self.showing = not self.showing
					child.select()
					return child
			return None
				
	def add_source_button(self, srcbutton):
		srcbutton.position = (0, 0)
		srcbutton.alpha = 0
		self.add_child(srcbutton)
		self.source_buttons.append(srcbutton)
		
	def update_from_sourceList(self, sourceList):
		for s in self.source_buttons:
			if not s.source in sourceList.sources_by_category[self.category.name]:
				self.source_buttons.remove(s)
				s.remove_from_parent()
		for s in sourceList.sources_by_category[self.category.name]:
			#if not s in self.source_buttons:
			if s.dirty:
				btn = SourceButton(s)
				self.source_buttons.append(btn)
				btn.alpha = 0
				self.add_child(btn)
				s.dirty = False
		
			
		



if __name__ == '__main__':

	class SmartDormApp (Scene):
		def setup(self):
			self.background_color = '#203040'
			self.btn = CategoryButton('#8fdbe8', SpriteNode('iow:bluetooth_32'))
			self.btn.position = (70, 130)
			
			self.add_child(self.btn)
			
			btn2 = CategoryButton("#8f8fff", SpriteNode('iow:beaker_32'))
			self.btn.add_source_button(btn2)
			
			btn3 = CategoryButton("#d8e77c", SpriteNode('iow:archive_32'))
			self.btn.add_source_button(btn3)
			
			btn4 = CategoryButton("#e77c9b", SpriteNode('iow:alert_circled_32'))
			self.btn.add_source_button(btn4)
			
		def touch_began(self, touch):
			if self.btn.collide(touch):
				self.btn.touched(touch)
			
	run(SmartDormApp(), PORTRAIT, show_fps=False)

