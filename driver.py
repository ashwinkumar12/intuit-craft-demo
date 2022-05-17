from node import Node
from vector_of_roots import VectorOfRoots
from binary_tree import BinaryTree

def construct_binary_tree():
	binary_tree = BinaryTree(1)

	binary_tree.add_left_node(binary_tree.get_root(), Node(2))
	binary_tree.add_right_node(binary_tree.get_root(), Node(3))

	binary_tree.add_left_node(binary_tree.get_root().get_left_node(), Node(4))
	binary_tree.add_right_node(binary_tree.get_root().get_left_node(), Node(5))
	binary_tree.add_left_node(binary_tree.get_root().get_right_node(), Node(6))
	binary_tree.add_right_node(binary_tree.get_root().get_right_node(), Node(7))

	return binary_tree

def print_vector_roots(roots):
	print("Vector of roots of subtrees : ")
	for root in roots:
		print(root.get_id(), end=" ")
	print()

def print_line_separator():
	print("--------------------------")

if __name__ == '__main__':
	binary_tree = construct_binary_tree()

	print("Tree - Inorder traversal")
	binary_tree.print_tree_inorder(binary_tree.get_root())
	print()
	print_line_separator()
	print("Press ENTER to QUIT")
	print_line_separator()

	while True:
		print()
		print("Enter the ID TO DELETE")
		id_to_delete = input().strip()
		if id_to_delete == "":
			break
		id_to_delete = int(id_to_delete)
		roots = VectorOfRoots().find_vector_of_roots(binary_tree.get_root(), id_to_delete)
		print_vector_roots(roots)
		

		