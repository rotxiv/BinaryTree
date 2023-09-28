from BinaryNode import*

class BinaryTree(object):
	"""docstring for BinaryTree"""
	def __init__(self):
		self.root = None

	def isEmptyTree(self):
		return BinaryNode.isEmptyNode(self.root)

	def insert(self, key, value):
		if BinaryNode.isEmptyNode(self.root):
			self.root = BinaryNode(key, value)
		else:
			self.__recursiveInsert(node, key, value)

	def __recursiveInsert(self, node, key, value):
		if key < node.key:
			if BinaryNode.isEmptyNode(node.leftSon):
				node.leftSon = BinaryNode(key, value)
			else:
				self.__recursiveInsert(node.leftSon, key, value)
		else:
			if BinaryNode.isEmptyNode(node.rightSon):
				node.rightSon = BinaryNode(key, value)
			else:
				self.__recursiveInsert(node.rightSon, key, value)

	def search(self):
		


arbol = BinaryTree()
print(arbol.isEmptyTree())
arbol.insert(10, "Hola Mundo...!")
print(arbol.isEmptyTree())
print(arbol.root.value)
