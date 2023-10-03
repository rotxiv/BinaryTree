class BinaryNode(object):
	"""docstring for BinaryNode"""
	def __init__(self, key, value):
		self.key = key
		self.value = value
		self.leftSon = None
		self.rightSon = None
		
	@staticmethod
	def isEmptyNode(node):
		return node == None

	def isLeaf(self):
		return (self.rightSon == None and self.leftSon == None)

"""
node = BinaryNode(10, "Hola Mundo...!")
print(node.value)
print(node.isLeaf())
"""
