from __future__ import annotations

from dataclasses import dataclass
from typing import Optional


@dataclass(frozen=True)
class Node:
    val: int
    left: Optional["Node"] = None
    right: Optional["Node"] = None


def search(tree: Optional[Node], x: int) -> bool:
    """
    Return True if x exists in the BST, otherwise False.
    """
    if tree is None:
        return False
    if x == tree.val:
        return True
    if x < tree.val:
        return search(tree.left, x)
    return search(tree.right, x)
    


def insert(tree: Optional[Node], x: int) -> Optional[Node]:
    """
    Insert x into the BST and return the updated tree.

    Duplicate values are ignored and the original tree is returned unchanged.
    """
    if tree is None:
        return Node(x)

    if x < tree.val:
        return Node(tree.val, insert(tree.left, x), tree.right)
    if x > tree.val:
        return Node(tree.val, tree.left, insert(tree.right, x))

    return tree


def delete(tree: Optional[Node], x: int) -> Optional[Node]:
    """
    Delete x from the BST and return the updated tree.

    If the node has two children, replace it with its inorder successor
    (the smallest value in the right subtree).
    """
    if tree is None:
        return None

    if x < tree.val:
        return Node(tree.val, delete(tree.left, x), tree.right)

    if x > tree.val:
        return Node(tree.val, tree.left, delete(tree.right, x))

    # Found the node to delete
    if tree.left is None and tree.right is None:
        return None

    if tree.left is None:
        return tree.right

    if tree.right is None:
        return tree.left

    # Two children: replace with inorder successor
    successor_val = _find_min(tree.right)
    new_right = delete(tree.right, successor_val)
    return Node(successor_val, tree.left, new_right)


def _find_min(tree: Node) -> int:
    """
    Return the minimum value in a non-empty BST.
    """
    current = tree
    while current.left is not None:
        current = current.left
    return current.val