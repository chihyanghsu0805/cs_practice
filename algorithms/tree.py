"""Algorithms for Tree."""
from __future__ import absolute_import, print_function

from typing import List


class Node:
    """Constructor."""

    def __init__(self, value: int) -> None:
        """Initialize Class.

        Args:
            value (int): Value to store in code.
        """
        self.value = value
        self.lt = None
        self.rt = None


def find_min_depth(root: Node) -> int:
    """Find Minimum Depth.

    Args:
        root (Node): root of Tree.

    Returns:
        int: Minimum depth.
    """
    if not root:
        return 0

    queue = []
    queue.append((root, 1))

    while queue:

        node, curr_d = queue.pop(0)

        if not node.lt and not node.rt:
            return curr_d

        if node.lt:
            queue.append((node.lt, curr_d + 1))

        if node.rt:
            queue.append((node.rt, curr_d + 1))


def find_min_depth2(root: Node) -> int:
    """Find Minimum Depth.

    Args:
        root (Node): root of Tree.

    Returns:
        int: Minimum depth.
    """
    if not root:
        return 0

    if not root.lt and not root.rt:
        return 1

    if root.lt:
        lt_d = 1 + find_min_depth2(root.lt)

    if root.rt:
        rt_d = 1 + find_min_depth2(root.rt)

    return min(lt_d, rt_d)


def find_max_path_sum(root: Node) -> List:
    """Find Maximum Path Sum.

    Args:
        root (Node): Root of Tree.

    Returns:
        List: Maximum path sum, Maximum sum including root.
    """
    if not root:
        # max_so_far should not be 0 for trees with only negative values
        # max_so_far, max_end_here
        return -float("inf"), 0

    lt_so_far, lt_end_here = find_max_path_sum(root.lt)
    rt_so_far, rt_end_here = find_max_path_sum(root.rt)

    max_end_here = max(0, max(lt_end_here, rt_end_here) + root.value)
    max_so_far = max(lt_end_here + rt_end_here + root.value, lt_so_far, rt_so_far)

    return max_so_far, max_end_here


def check_array_preorder_tree(arr: List) -> bool:
    """Check Array is Preorder of Tree.

    Args:
        arr (List): Given array.

    Returns:
        bool: True if array is preorder.
    """
    stack = []
    min_value = -float("inf")

    for value in arr:

        if value < min_value:
            return False

        while len(stack) > 0 and stack[-1] < value:
            min_value = stack.pop()

        stack.append(value)

    return True


def check_full_binary_tree(root: Node) -> bool:
    """Check Full Binary Tree.

    Args:
        root (Node): root of tree.

    Returns:
        bool: tree is full.
    """
    if not root:
        return True

    if not root.lt and not root.rt:
        return True

    if root.lt and root.rt:
        return check_full_binary_tree(root.lt) and check_full_binary_tree(root.rt)

    return False


def view_bottom(root: Node) -> List:
    """View from Bottom.

    Args:
        root (Node): root of tree.

    Returns:
        List: bottom view.
    """
    if not root:
        return []

    horizontal_d = 0
    map = {}
    queue = []
    queue.append((root, horizontal_d))

    while queue:

        node, d = queue.pop(0)
        map[d] = node.value

        if node.lt:
            queue.append((node.lt, d - 1))

        if node.rt:
            queue.append((node.rt, d + 1))

    return [map[i] for i in sorted(map.keys())]


def view_top(root: Node) -> List:
    """View from Top.

    Args:
        root (Node): root of tree.

    Returns:
        List: Top view.
    """
    if not root:
        return []

    horizontal_d = 0
    map = {}
    queue = []
    queue.append((root, horizontal_d))

    while queue:

        node, d = queue.pop(0)
        if d not in map:
            map[d] = node.value

        if node.lt:
            queue.append((node.lt, d - 1))

        if node.rt:
            queue.append((node.rt, d + 1))

    return [map[i] for i in sorted(map.keys())]


def remove_node_on_path(root: Node, k: int) -> Node:
    """Remove Node on Path Shorter than K.

    Args:
        root (Node): root of tree.
        k (int): path length threshold.

    Returns:
        Node: root of tree.
    """

    def helper(root, k, d):
        if not root:
            return None
        root.lt = helper(root.lt, k, d + 1)
        root.rt = helper(root.rt, k, d + 1)

        if not root.lt and not root.rt and d < k:
            return None

        return root

    return helper(root, k, 1)


def inorder(root: Node) -> List:
    """Traverse Inorder.

    Args:
        root (Node): Root of tree.

    Returns:
        List: inorder value array.
    """
    arr = []
    current = root
    stack = []
    while True:

        if current:
            stack.append(current)
            current = current.lt

        elif stack:
            current = stack.pop()
            arr.append(current.value)
            current = current.rt

        else:
            break

    return arr


def find_lowest_common_ancestor(root: Node, v1: int, v2: int) -> Node:
    """Find Lowest Common Ancestor in BST.

    Args:
        root (Node): root of tree.
        v1 (int): first value.
        v2 (int): second value.

    Returns:
        Node: Lowest Common Ancestor.
    """
    if not root:
        return None

    if v1 < root.value and v2 < root.value:
        return find_lowest_common_ancestor(root.lt, v1, v2)

    if v1 > root.value and v2 > root.value:
        return find_lowest_common_ancestor(root.rt, v1, v2)

    return root


def check_subtree(root1: Node, root2: Node) -> bool:
    """Check Root1 is Subtree of Root2.

    Args:
        root1 (Node): root of first tree.
        root2 (Node): root of second tree.

    Returns:
        bool: True if root1 is subtree of root2.
    """
    return preorder(root1) in preorder(root2)


def preorder(root: Node) -> str:
    """Traverse Inorder.

    Args:
        root (Node): Root of tree.

    Returns:
        str: preorder string.
    """
    return (
        "^" + str(root.value) + preorder(root.lt) + preorder(root.rt) if root else "#"
    )


def reverse_alternate_level(root: Node) -> None:
    """Reverse Alternate Level.

    Args:
        root (Node): Root of tree.
    """

    def helper(root1, root2, depth):

        if not root1 and not root2:
            return

        if depth % 2 == 0:
            root1.value, root2.value = root2.value, root1.value

        helper(root1.lt, root2.rt, depth + 1)
        helper(root1.rt, root2.lt, depth + 1)

    helper(root.lt, root.rt, 0)


if __name__ == "__main__":

    root = Node(1)
    root.lt = Node(2)
    root.rt = Node(3)
    root.lt.lt = Node(4)
    root.lt.rt = Node(5)
    assert find_min_depth(root) == 2
    assert find_min_depth2(root) == 2

    root = Node(10)
    root.lt = Node(2)
    root.rt = Node(10)
    root.lt.lt = Node(20)
    root.lt.rt = Node(1)
    root.rt.rt = Node(-25)
    root.rt.rt.lt = Node(3)
    root.rt.rt.rt = Node(4)
    assert find_max_path_sum(root)[0] == 42

    arr = [40, 30, 35, 80, 100]
    assert check_array_preorder_tree(arr)
    arr = [40, 30, 35, 20, 80, 100]
    assert not check_array_preorder_tree(arr)

    root = Node(10)
    root.lt = Node(20)
    root.rt = Node(30)

    root.lt.rt = Node(40)
    root.lt.lt = Node(50)
    root.rt.lt = Node(60)
    root.rt.rt = Node(70)

    root.lt.lt.lt = Node(80)
    root.lt.lt.rt = Node(90)
    root.lt.rt.lt = Node(80)
    root.lt.rt.rt = Node(90)
    root.rt.lt.lt = Node(80)
    root.rt.lt.rt = Node(90)
    root.rt.rt.lt = Node(80)

    assert not check_full_binary_tree(root)
    root.rt.rt.rt = Node(90)
    assert check_full_binary_tree(root)

    root = Node(1)
    root.lt = Node(2)
    root.rt = Node(3)
    root.lt.lt = Node(4)
    root.lt.rt = Node(5)
    root.rt.lt = Node(6)
    root.rt.rt = Node(7)
    assert view_bottom(root) == [4, 2, 6, 3, 7]
    assert view_top(root) == [4, 2, 1, 3, 7]

    k = 4
    root = Node(1)
    root.lt = Node(2)
    root.rt = Node(3)
    root.lt.lt = Node(4)
    root.lt.rt = Node(5)
    root.lt.lt.lt = Node(7)
    root.rt.rt = Node(6)
    root.rt.rt.lt = Node(8)

    assert inorder(remove_node_on_path(root, k)) == [7, 4, 2, 1, 3, 8, 6]

    root = Node(20)
    root.lt = Node(8)
    root.rt = Node(22)
    root.lt.lt = Node(4)
    root.lt.rt = Node(12)
    root.lt.rt.lt = Node(10)
    root.lt.rt.rt = Node(14)
    v1, v2 = 10, 14
    assert find_lowest_common_ancestor(root, v1, v2).value == 12
    v1, v2 = 8, 14
    assert find_lowest_common_ancestor(root, v1, v2).value == 8
    v1, v2 = 10, 22
    assert find_lowest_common_ancestor(root, v1, v2).value == 20

    root1 = Node("A")
    root1.lt = Node("B")
    root1.rt = Node("D")
    root1.lt.lt = Node("C")
    root1.rt.rt = Node("E")

    root2 = Node("A")
    root2.lt = Node("B")
    root2.rt = Node("D")
    root2.lt.lt = Node("C")

    assert not check_subtree(root2, root1)

    root = Node("a")
    root.lt = Node("b")
    root.rt = Node("c")
    root.lt.lt = Node("d")
    root.lt.rt = Node("e")
    root.rt.lt = Node("f")
    root.rt.rt = Node("g")
    root.lt.lt.lt = Node("h")
    root.lt.lt.rt = Node("i")
    root.lt.rt.lt = Node("j")
    root.lt.rt.rt = Node("k")
    root.rt.lt.lt = Node("l")
    root.rt.lt.rt = Node("m")
    root.rt.rt.lt = Node("n")
    root.rt.rt.rt = Node("o")

    reverse_alternate_level(root)
    assert inorder(root) == [
        "o",
        "d",
        "n",
        "c",
        "m",
        "e",
        "l",
        "a",
        "k",
        "f",
        "j",
        "b",
        "i",
        "g",
        "h",
    ]
