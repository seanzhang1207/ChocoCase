class Link (object):

	def __init__(self, src, out, dest):
		self.src = src
		self.dest = dest
		self.out = out
		self.running = False
