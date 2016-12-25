from scene import *

from gui.SourceManager import SourceManager
from gui.CategoryButton import CategoryButton
from gui.OutletManager import OutletManager
from gui.OutletButton import OutletButton
from gui.LinkManager import LinkManager
from gui.DestinationManager import DestinationManager
from gui.DestinationButton import DestinationButton
from gui.DestinationWindow import DestinationWindow

from data.Source import Source
from data.Category import Category
from data.Outlet import Outlet
from data.Destination import Destination

class UserInterface (Node):
	
	def setup(self):
		self.inputing = False
		
		self.sourceManager = SourceManager()
		self.linkManager = LinkManager()
		self.outletManager = OutletManager()
		self.destinationManager = DestinationManager()
		
		self.add_child(self.sourceManager)
		self.add_child(self.outletManager)
		self.add_child(self.linkManager)
		self.add_child(self.destinationManager)
		
		self.sourceManager.add_category_button(CategoryButton(Category('phone')))
		#self.sourceManager.add_category_button(CategoryButton(Category('bluetooth')))
		self.sourceManager.add_category_button(CategoryButton(Category('module')))
		
		self.outletManager.add_outlet_button(OutletButton(Outlet('wifi')))
		
		self.overlay = ShapeNode(ui.Path.rect(0, 0, 800, 400), '#000000')
		self.overlay.position = (400, 200)
		self.overlay.alpha = 0
		self.overlay.ignore = True
		self.add_child(self.overlay)
		
		self.state = 'init'
		self.currentDestination = None
		self.currentOutlet = None
		self.currentSource = None

	def show_overlay(self):
		self.overlay.run_action(Action.fade_to(0.3, 0.3, TIMING_EASE_OUT))
	
	def hide_overlay(self):
		self.overlay.run_action(Action.fade_to(0.0, 0.3, TIMING_EASE_OUT))
	
	def update_with_sourcelist(self, sourceList):
		self.sourceManager.update_from_sourcelist(sourceList)
		#self.outletManager.update_from_sourcelist(sourceList)
		#self.destinationManager.update_destinations_from_sourceList(sourceList)
		self.linkManager.update_from_sourcelist(sourceList)
	
	def touch_began(self, touch):
		if self.inputing:
			ip = self.ipWindow.touched(touch)
			if ip:
				self.inputing = False
				print(ip)
				self.currentDestination = DestinationButton(Destination('wifi', addr=ip))
				self.destinationManager.add_destination_button(self.currentDestination)
				self.destinationManager.show_destinations_for_outlet(None)
				self.linkManager.clear_templinks()
				self.linkManager.add_permalink(self.currentSource, self.currentOutlet, self.currentDestination)
				self.currentDestination.linked = self.currentDestination.linked + 1
				self.currentOutlet.linked = self.currentOutlet.linked + 1
				self.state = 'init'
				self.destinationManager.hide_destinations()
			return
		if self.state == 'init':
			src = self.sourceManager.touched(touch)
			if src:
				self.state = 'outlet'
				self.currentSource = src
				self.outletManager.show_outlets_for_source(src)
			else:
				pass
		
		elif self.state == 'outlet':
			out = self.outletManager.touched(touch)
			if out:
				self.state = 'destination'
				self.currentOutlet = out
				#self.outletManager.hide_outlets()
				self.linkManager.add_templink(self.currentSource, self.currentOutlet)
				self.sourceManager.hide_all_sources()
				self.currentOutlet.linked = self.currentOutlet.linked + 1
				self.destinationManager.show_destinations_for_outlet(None)
			else:
				self.state = 'init'
				self.sourceManager.hide_all_sources()
				self.outletManager.hide_outlets()
				self.linkManager.clear_templinks()
				self.currentOutlet.linked = self.currentOutlet.linked - 1
				self.hide_overlay()
		elif self.state == 'destination':
			dest = self.destinationManager.touched(touch)
			if dest == 'input':
				self.ipWindow = DestinationWindow()
				self.ipWindow.position = self.scene.size/2
				self.add_child(self.ipWindow)
				self.inputing = True
			elif dest:
				self.state = 'init'
				self.currentDestination = dest
				self.linkManager.add_permalink(self.currentSource, self.currentOutlet, self.currentDestination)
				self.currentDestination.linked = self.currentDestination.linked + 1
				self.destinationManager.hide_destinations()
				self.outletManager.hide_outlets()
				self.linkManager.clear_templinks()
				self.currentDestination = None
				self.currentOutlet = None
				self.currentSource = None
			else:
				self.state = 'init'
				self.currentOutlet.linked = self.currentOutlet.linked - 1
				self.linkManager.clear_templinks()
				self.sourceManager.hide_all_sources()
				self.outletManager.hide_outlets()
				self.destinationManager.hide_destinations()
				self.currentDestination = None
				self.currentOutlet = None
				self.currentSource = None

	def draw(self):
		self.linkManager.draw()
	
