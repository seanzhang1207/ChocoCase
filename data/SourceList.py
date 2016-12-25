class SourceList (object):
	
	def __init__(self):
		self.sources = []
		self.dirty = False
		self.data = None
		self.sources_by_category = {
			'phone': [],
			'module': [], 
		}
		
	def add(self, src):
		self.sources.append(src)
		self.sources_by_category[src.category].append(src)
		self.dirty = True
		
	def remove(self, src):
		self.sources.remove(src)
		self.sources_by_category[src.category].remove(src)
		self.dirty = True
		
	def find_source_at_port(self, port):
		for s in self.sources:
			try:
				if s.port == port:
					return s
			except:
				pass
		return None
