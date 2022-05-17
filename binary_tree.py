from node import Node

class BinaryTree:

	def __init__(self, id):
		self.root = Node(id)

	def get_root(self):
		return self.root

	def add_left_node(self, node, node_to_add):
		node.left = node_to_add

	def add_right_node(self, node, node_to_add):
		node.right = node_to_add

	def get_root(self):
		return self.root

	def print_tree_inorder(self, node):
		if node:
			self.print_tree_inorder(node.left)
			print(node.id, end =" ")
			self.print_tree_inorder(node.right)

	def print_tree_preorder(self, node):
		if node:
			print(node.id, end =" ")
			self.print_tree_preorder(node.left)
			self.print_tree_preorder(node.right)

	def print_tree_postorder(self, node):
		if node:
			self.print_tree_postorder(node.left)
			self.print_tree_postorder(node.right)
			print(node.id, end =" ")
