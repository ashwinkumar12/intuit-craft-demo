"""
Given a binary tree with unique integer values. Return the vector of roots of subtrees formed after
removing the given node.

Node {
	int id;
	Node left;
	Node right;
};

Vector<Integer> removeNode(Node root, int nodeToBeRemoved)
"""
class VectorOfRoots:

	def __init__(self):
		self.vector_of_roots  = set()

	def find_vector_of_roots(self, root, id_to_delete):
		self.dfs(root, root, id_to_delete)
		return self.vector_of_roots

	def add_to_vector_roots(self, sub_tree_root, id_to_delete):
		if sub_tree_root and sub_tree_root.get_id() != id_to_delete:
			self.vector_of_roots.add(sub_tree_root)

	def dfs(self, root, sub_tree_root, id_to_delete):
		if not root: 
			return self.add_to_vector_roots(sub_tree_root, id_to_delete)

		if root.get_id() == id_to_delete:
			self.add_to_vector_roots(sub_tree_root, id_to_delete)
			sub_tree_root_left = root.get_left_node()
			sub_tree_root_right = root.get_right_node()
		else:
			sub_tree_root_left = sub_tree_root_right = sub_tree_root

		self.dfs(root.get_left_node(), sub_tree_root_left, id_to_delete)
		self.dfs(root.get_right_node(), sub_tree_root_right, id_to_delete)