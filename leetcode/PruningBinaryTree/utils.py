from __future__ import annotations

from dataclasses import dataclass
from queue import Queue


@dataclass
class Node:
    val: int
    left: Node = None
    right: Node = None


def print_binary_tree(root: Node):
    """Prints the depth and breadth traversal of a binary tree

    Args:
        root (Node): root node of the tree to print
    """

    def breadth_traversal(root: Node):
        """Breadth traversal for a binary tree

        Args:
            root (Node): Root node of the tree
        """
        print("Breadth Traversal: ", end="")
        if root is None:
            return

        queue = Queue()
        queue.push(root)

        while queue.size() > 0:
            node = queue.pop()
            print(f"{node.val}, ", end="")

            if node.left is not None:
                queue.push(node.left)
            if node.right is not None:
                queue.push(node.right)
        print("")

    def depth_traversal(node: Node):
        """Depth Traversal of a binary tree

        Args:
            node (Node): Root of the binary tree
        """
        if node is None:
            return

        print(f"{node.val}, ", end="")
        depth_traversal(node.left)
        depth_traversal(node.right)

    breadth_traversal(root)
    print("Depth Traversal: ", end="")
    depth_traversal(root)
    print("")


def initialize_tree_0() -> Node:
    #       1
    #        \
    #         0
    #        / \
    #       0   1
    root = Node(1)
    root.right = Node(0)
    root.right.left = Node(0)
    root.right.right = Node(1)
    return root


def initialize_tree_1() -> Node:
    #       0
    #     /   \
    #    1     0
    #         / \
    #        1   0
    #      /  \
    #     0   0
    root = Node(0)
    root.left = Node(1)
    root.right = Node(0)
    root.right.left = Node(1)
    root.right.right = Node(0)
    root.right.left.left = Node(0)
    root.right.left.right = Node(0)
    return root


def initialize_tree_2() -> Node:
    #        1
    #      /   \
    #     0     1
    #   /  \   / \
    #  0   0  0   1
    root = Node(1)
    root.left = Node(0)
    root.right = Node(1)
    root.left.left = Node(0)
    root.left.right = Node(0)
    root.right.left = Node(0)
    root.right.right = Node(1)
    return root


def initialize_tree_3() -> Node:
    #           1
    #         /   \
    #        1     0
    #      /  \   / \
    #     1   1  0   1
    #   /
    #  0
    root = Node(1)
    root.left = Node(1)
    root.right = Node(0)
    root.left.left = Node(1)
    root.left.right = Node(1)
    root.left.left.left = Node(0)
    root.right.left = Node(0)
    root.right.right = Node(1)
    return root
