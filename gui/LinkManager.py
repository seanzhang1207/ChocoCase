from scene import *
from data.Link import Link

class LinkManager(Node):
	
	def __init__(self):
		self.templinks = []
		self.permalinks = []
		super(Node, self).__init__()
		
	def add_templink(self, src, dest):
		self.templinks.append((src, dest))
		
	def add_permalink(self, src, out, dest):
		link = Link(src, out, dest)
		self.permalinks.append(link)
		
	def clear_templinks(self):
		self.templinks = []
	
	def draw(self):
		for child in self.templinks:
			stroke(1, 1, 1)
			stroke_weight(4)
			x1 = child[0].parent.point_to_scene(child[0].position).x
			x2 = child[1].parent.point_to_scene(child[1].position).x
			y1 = child[0].parent.point_to_scene(child[0].position).y
			y2 = child[1].parent.point_to_scene(child[1].position).y
			
			line(x1, y1, x2, y2)
			
		for link in self.permalinks:
			stroke(1, 1, 1)
			stroke_weight(4)
			x1 = link.src.parent.point_to_scene(link.src.position).x
			x2 = link.out.parent.point_to_scene(link.out.position).x
			x3 = link.dest.parent.point_to_scene(link.dest.position).x
			y1 = link.src.parent.point_to_scene(link.src.position).y
			y2 = link.out.parent.point_to_scene(link.out.position).y
			y3 = link.dest.parent.point_to_scene(link.dest.position).y
			
			line(x1, y1, x2, y2)
			line(x2, y2, x3, y3)
			
	def update_from_sourcelist(self, sourceList):
		for l in self.templinks:
			if not l[0] in sourceList.sources:
				self.templinks.remove(l)
				l[1].linked = l[1].linked - 1
		for l in self.permalinks:
			if not l.src in sourceList.sources:
				self.permalinks.remove(l)
				l.out.linked = l.out.linked - 1
				l.dest.linked = l.dest.linked - 1

if __name__ == '__main__':

	class SmartDormApp (Scene):
		def setup(self):
			self.l = LinkManager()
			a = SpriteNode('typb:Archive')
			a.position = (100, 100)
			self.add_child(a)
			b = SpriteNode('typb:Battery_Full')
			b.position = (200, 200)
			self.add_child(b)
			self.add_child(self.l)
			self.l.add_link(a, b)
			
		def draw(self):
			self.l.draw()
			
			
	run(SmartDormApp(), LANDSCAPE, show_fps=False)
