from scene import *
from gui.uibase.TextRectButton import TextRectButton
from gui.uibase.LongTextRectButton import LongTextRectButton

class DestinationWindow (ShapeNode):

	def __init__(self):
		self.buttons = []
		self.current_phase = 'ip'
		self.current_ip_seg = 0
		
		self.background = ui.Path.rounded_rect(0, 0, 300, 300, 10)
		self.background.line_width = 0
		
		shadow = ('#80000000', 1, 1, 2)
		super(DestinationWindow, self).__init__(self.background, '#f2ebe8', 'silver', shadow=shadow)
		
		self.position = (0, -500)
		
		self.iptext = []
		
		i = LabelNode('XXX', font=('helvetica', 30), color='#d0d0d0')
		i.position = (-105, 100)
		self.add_child(i)
		self.iptext.append(i)
		
		i = LabelNode('XXX', font=('helvetica', 30), color='#d0d0d0')
		i.position = (-35, 100)
		self.add_child(i)
		self.iptext.append(i)
		
		i = LabelNode('XXX', font=('helvetica', 30), color='#d0d0d0')
		i.position = (35, 100)
		self.add_child(i)
		self.iptext.append(i)
		
		i = LabelNode('XXX', font=('helvetica', 30), color='#d0d0d0')
		i.position = (105, 100)
		self.add_child(i)
		self.iptext.append(i)
		
		self.dots = LabelNode('.      .      .', font=('helvetica', 36), color='#383838')
		self.dots.position = (0, 105)
		self.add_child(self.dots)
		
		self.porttext = LabelNode('', font=('helvetica', 30), color='#383838')
		self.porttext.position = (0, 100)
		self.add_child(self.porttext)
	
		
		btn = TextRectButton('#5277d5', '1')
		btn.position = (-105, 30)
		self.add_child(btn)
		self.buttons.append(btn)
		
		btn = TextRectButton('#5277d5', '2')
		btn.position = (-35, 30)
		self.add_child(btn)
		self.buttons.append(btn)
		
		btn = TextRectButton('#5277d5', '3')
		btn.position = (35, 30)
		self.add_child(btn)
		self.buttons.append(btn)
		
		btn = TextRectButton('#5277d5', '0')
		btn.position = (105, 30)
		self.add_child(btn)
		self.buttons.append(btn)
		
		btn = TextRectButton('#5277d5', '4')
		btn.position = (-105, -40)
		self.add_child(btn)
		self.buttons.append(btn)
		
		btn = TextRectButton('#5277d5', '5')
		btn.position = (-35, -40)
		self.add_child(btn)
		self.buttons.append(btn)
		
		btn = TextRectButton('#5277d5', '6')
		btn.position = (35, -40)
		self.add_child(btn)
		self.buttons.append(btn)
		
		self.dotbtn = TextRectButton('#7fbd66', '.')
		self.dotbtn.position = (105, -40)
		self.add_child(self.dotbtn)
		self.buttons.append(self.dotbtn)
		
		btn = TextRectButton('#5277d5', '7')
		btn.position = (-105, -110)
		self.add_child(btn)
		self.buttons.append(btn)
		
		btn = TextRectButton('#5277d5', '8')
		btn.position = (-35, -110)
		self.add_child(btn)
		self.buttons.append(btn)
		
		btn = TextRectButton('#5277d5', '9')
		btn.position = (35, -110)
		self.add_child(btn)
		self.buttons.append(btn)
		
		self.nextbtn = TextRectButton('#5ac3d5', 'Next')
		self.nextbtn.position = (105, -110)
		self.add_child(self.nextbtn)
		self.buttons.append(self.nextbtn)
		
		self.donebtn = TextRectButton('#d55277', 'Done')
		self.donebtn.position = (105, -110)
		self.donebtn.alpha = 0
		self.add_child(self.donebtn)
		self.buttons.append(self.donebtn)
		
		self.ip = ['', '', '', '']
		self.port = ''

	def touched(self, touch):
		for btn in self.buttons:
			if btn.collide(touch) and btn.alpha == 1:
				if self.current_phase == 'ip':
					if btn.text == '.':
						self.current_ip_seg = self.current_ip_seg + 1
					elif btn.text == 'Next':
						if self.current_ip_seg > 3:
							self.current_ip_seg = 3
						if len(self.ip[self.current_ip_seg]) > 0:
							self.current_phase = 'port'
							for t in self.iptext:
								t.alpha = 0
							self.dots.alpha = 0
							self.nextbtn.alpha = 0
							self.donebtn.alpha = 1
							self.dotbtn.alpha = 0.4
					else:
						if self.current_ip_seg <= 3:
							if len(self.ip[self.current_ip_seg]) < 3:
								if len(self.ip[self.current_ip_seg]) == 0:
									self.iptext[self.current_ip_seg].color = '#363636'
								self.ip[self.current_ip_seg] = self.ip[self.current_ip_seg] + btn.text
								self.iptext[self.current_ip_seg].text = self.ip[self.current_ip_seg]
							else:
								self.current_ip_seg = self.current_ip_seg + 1
								if self.current_ip_seg < 4:
									self.ip[self.current_ip_seg] = self.ip[self.current_ip_seg] + btn.text
									self.iptext[self.current_ip_seg].color = '#363636'
									self.iptext[self.current_ip_seg].text = self.ip[self.current_ip_seg]
				elif self.current_phase == 'port':
					if btn.text == 'Done':
						if len(self.port) > 0:
							self.hide()
							return (self.ip[0]+'.'+self.ip[1]+'.'+self.ip[2]+'.'+self.ip[3], int(self.port))
					else:
						if len(self.port) < 5:
							self.port = self.port + btn.text
							self.porttext.text = self.port
	def show(self):
		self.run_action(Action.move_by(0, 500, 0.5, TIMING_EASE_OUT))
		
	def hide(self):
		self.run_action(Action.move_by(0, -500, 0.5, TIMING_EASE_OUT))

		
		
		
if __name__ == '__main__':

	class SmartDormApp (Scene):
		def setup(self):
			self.btn = DestinationWindow()
			self.btn.position = self.scene.size/2
			self.add_child(self.btn)
			
			
		def touch_began(self, touch):
			self.btn.touched(touch)
		
			
	run(SmartDormApp(), LANDSCAPE, show_fps=False)
