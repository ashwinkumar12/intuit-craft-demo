class Node:

	def __init__(self, id, left=None, right=None):
		self.id = id
		self.left = left
		self.right = right

	def get_id(self):
		return self.id

	def get_left_node(self):
		return self.left

	def get_right_node(self):
		return self.right

	def set_left_node(self, node):
		self.left = node
		return self

	def set_right_node(self, node):
		self.right = node
		return self
