from BinaryNode import*

class BinaryTree(object):
	"""docstring for BinaryTree"""
	def __init__(self):
		self.root = None

	def isEmptyTree(self):
		return BinaryNode.isEmptyNode(self.root)

	def clear(self):
		self.root = None

	def insert(self, key, value):
		if BinaryNode.isEmptyNode(self.root):
			self.root = BinaryNode(key, value)
		else:
			self.__recursiveInsert(self.root, key, value)

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
		pass	
	
	def inOrden(self):
		listInOrden = []
		self.__inOrden(self.root, listInOrden)
		return listInOrden

	def __inOrden(self, node, listInOrden):
		if not BinaryNode.isEmptyNode(node):
			self.__inOrden(node.leftSon, listInOrden)
			listInOrden.append(node.key)
			self.__inOrden(node.rightSon, listInOrden)

	def posOrden(self):
		listPosOrden = []
		self.__posOrden(self.root, listPosOrden)
		return listPosOrden

	def __posOrden(self, node, listPosOrden):
		if not BinaryNode.isEmptyNode(node):
			self.__posOrden(node.leftSon, listPosOrden)
			self.__posOrden(node.rightSon, listPosOrden)
			listPosOrden.append(node.key)

	def preOrden(self):
		listPreOrden = []
		self.__preOrden(self.root, listPreOrden)
		return listPreOrden

	def __preOrden(self, node, listPreOrden):
		if not BinaryNode.isEmptyNode(node):
			listPreOrden.append(node.key)
			self.__preOrden(node.leftSon, listPreOrden)
			self.__preOrden(node.rightSon, listPreOrden)


arbol = BinaryTree()
arbol.insert(10, "Santa Cruz")
arbol.insert(20, "La Paz")
arbol.insert(5, "Cochabamba")
arbol.insert(7, "Tarija")
arbol.insert(15, "Potosi")
print("recorrido en inOrden : ")
print(arbol.inOrden())
print("recorrido en preOrden : ")
print(arbol.preOrden())
print("recorrido en posOrden : ")
print(arbol.posOrden())
