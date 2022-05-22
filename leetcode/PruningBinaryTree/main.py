from __future__ import annotations

from queue import Queue

from utils import (
    Node,
    initialize_tree_0,
    initialize_tree_1,
    initialize_tree_2,
    initialize_tree_3,
    print_binary_tree,
)


def check_all_zeros_tree(root: Node):
    queue = Queue()
    queue.push(root)

    while queue.size() > 0:
        node = queue.pop()
        if node.val == 1:
            return False

        if node.left is not None:
            queue.push(node.left)
        if node.right is not None:
            queue.push(node.right)

    return True


def prune_binary_tree(root: Node):
    queue = Queue()
    queue.push(root)

    while queue.size() > 0:
        node = queue.pop()

        if node.left is not None:
            if check_all_zeros_tree(root=node.left):
                node.left = None
        if node.right is not None:
            if check_all_zeros_tree(root=node.right):
                node.right = None

        if node.left is not None:
            queue.push(node.left)
        if node.right is not None:
            queue.push(node.right)

    return root


def main() -> None:
    for root in [
        initialize_tree_0(),
        initialize_tree_1(),
        initialize_tree_2(),
        initialize_tree_3(),
    ]:
        print("-------------------")
        print("Before Pruning")
        print_binary_tree(root)
        root = prune_binary_tree(root)

        print("\nAftering Pruning")
        print_binary_tree(root)
        print("")


if __name__ == "__main__":
    main()
