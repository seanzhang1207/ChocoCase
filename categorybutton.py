from scene import *
from roundedrectbutton import RoundRectButton

class CategoryButton (RoundRectButton):
    def __init__(self, color, icon, data):
        self.data = data
        self.source_buttons = []
        super(RoundRectButton, self).__init__('#d9e87d', icon)

    def touched(self, touch):
        self.showing = not self.showing
        if self.showing:
            for i in range(len(self.sources)):
                child = self.children[i]
                x = self.position[0] + 40
                y = self.position[1] + (len(self.children)/2.0 - i) * 80
                child.run_action(Action.group(Action.fade_to(1.0, 0.3, TIMING_EASE_OUT), Action.move_to(x, y, 0.3, TIMING_EASE_OUT)))
        else:
            for child in self.sources:
                child.run_action(Action.group(Action.fade_to(1.0, 0.3, TIMING_EASE_OUT), Action.move_to(self.position[0], self.position[1], 0.3, TIMING_EASE_OUT)))

    def add_source_button(srcbutton):
        self.source_buttons.append(srcbutton)



"""
class WifiCategoryButton (CategoryButton):
	def __init__(self):
		self.category = 'wifi'
		icon = SpriteNode('iow:wifi_32')
		icon.position = (-2, 2)
		super(WifiCategoryButton, self).__init__('#d9e87d', icon)

class BluetoothCategoryButton (CategoryButton):
	def __init__(self):
		self.category = 'bluetooth'
		icon = SpriteNode('iow:bluetooth_32')
		icon.position = (-2, 2)
		super(BluetoothCategoryButton, self).__init__('#8fdbe8', icon)

class SensorCategoryButton (CategoryButton):
	def __init__(self, icon='iow:arrow_shrink_32'):
		self.category = 'sensor'
		icon=SpriteNode(icon)
		icon.position = (-2, 2)
		super(SensorCategoryButton, self).__init__('#ffd193', icon)

class CameraCategoryButton (CategoryButton):
	def __init__(self):
		self.category = 'camera'
		icon=SpriteNode('iow:camera_32')
		icon.position = (-2, 2)
		super(CameraCategoryButton, self).__init__('#e9baf1', icon)

class MicrophoneCategoryButton (CategoryButton):
	def __init__(self):
		self.category = 'microphone'
		icon=SpriteNode('iow:mic_a_32')
		icon.position = (-2, 2)
		super(MicrophoneCategoryButton, self).__init__('#9df0cd', icon)
"""



if __name__ == '__main__':

	class SmartDormApp (Scene):
		def setup(self):
			self.background_color = '#203040'
			btn = CategoryButton('#8fdbe8', SpriteNode('iow:bluetooth_32'), )
			btn.position = (70, 70)

			self.add_child(btn)

	run(SmartDormApp(), PORTRAIT, show_fps=False)
