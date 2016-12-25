from gui.CategoryButton import CategoryButton
from scene import *

class SourceManager (Node):
	
	def __init__(self):
		self.in_category = False
		self.categories = []
		
	def add_category_button(self, btn):
		btn.alpha = 0.4
		self.add_child(btn)
		self.categories.append(btn)
		
		for i in range(len(self.categories)):
			y = self.scene.size.h/2 + (len(self.categories)/2 -1.5 - i+1)*80
			self.categories[i].run_action(Action.move_to(50, y, 0.3, TIMING_EASE_OUT))

	def hide_all_sources(self):
		self.in_category = False
		for child in self.categories:
			child.hide_sources()

	def touched(self, touch):
		if not self.in_category:
			for child in self.categories:
				if child.collide(touch):
					child.touched(touch)
					self.in_category = True
					self.current_category = child
					return None
			return None
		else:
			src = self.current_category.touched(touch)
			if src:
				self.in_category = False
				src.scale = 1.1
				#	child.hide_sources()
				return src
			for child in self.categories:
				child.hide_sources()
			self.in_category = False
			self.current_category = None
			return None

	def update_from_sourcelist(self, sourceList):
		for cat in self.categories:
			if len(sourceList.sources_by_category[cat.category.name]) == 0:
				cat.run_action(Action.fade_to(0.4, 0.3, TIMING_EASE_OUT))
			else:
				cat.run_action(Action.fade_to(1.0, 0.3, TIMING_EASE_OUT))
			cat.update_from_sourceList(sourceList)
