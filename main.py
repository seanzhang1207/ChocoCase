from scene import *
from threading import Thread

from gui.UserInterface import UserInterface

from data.Source import Source
from data.SourceList import SourceList
from data.Outlet import Outlet
#from data.OutletList import OutletList
from data.Destination import Destination
#from data.DestinationList import DestinationList
from data.Link import Link

from ModuleServer import ModuleServer
from JobServer import JobServer

class ChocoCaseApp (Scene):
	
	def setup(self):
		
		self.sourceList = SourceList()
		self.outletList = []
		self.destinationList = []
		
		self.sourceList.add(Source('gps'))
		self.sourceList.add(Source('gyro'))
		self.sourceList.add(Source('ambientlight'))
		
		self.moduleServer = Thread(target=ModuleServer, args=('ModuleServer', self.sourceList))
		
		self.ui = UserInterface()
		self.add_child(self.ui)
		self.ui.setup()
		
		self.jobServer = Thread(target=JobServer, args=('JobServer', self.ui.linkManager.permalinks))
		
		self.moduleServer.start()
		self.jobServer.start()
		
	def touch_began(self, touch):
		self.ui.touch_began(touch)
		
	def draw(self):
		self.ui.draw()
		
	def update(self):
		if self.sourceList.dirty:
			#print(self.sourceList.sources)
			self.sourceList.dirty = False
			#self.linkList.update_with_sources(self.sourceList)
			self.ui.update_with_sourcelist(self.sourceList)
		
	def pause(self):
		print('pause')
		
	def resume(self):
		print('resume')
	
	def stop(self):
		print('stop')

run(ChocoCaseApp(), LANDSCAPE, show_fps=False)
