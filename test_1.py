import unittest

from lab6_1 import Node, search, insert, delete


class TestSearch(unittest.TestCase):
    def test_search_finds_existing_value(self):
        root = Node(10, left=Node(5), right=Node(15))

        self.assertTrue(search(root, 10))
        self.assertTrue(search(root, 5))
        self.assertTrue(search(root, 15))
        pass

    def test_search_returns_false_for_missing_value(self):
        root = Node(10, left=Node(5), right=Node(15))

        self.assertFalse(search(root, 23))
        self.assertFalse(search(root, 12))

        pass

    def test_search_on_empty_tree(self):
        root = None

        self.assertFalse(search(root, 10))
        pass


class TestInsert(unittest.TestCase):
    def test_insert_into_empty_tree(self):
        root = None
        root = insert(root, 10)



        self.assertIsNotNone(root)
        self.assertEqual(root.val, 10)
        pass

    def test_insert_new_value_in_correct_position(self):
         root = Node(10)
         root = insert(root, 5)
         root = insert(root, 15)

         self.assertEqual (root.val, 10)
         self.assertIsNotNone(root.left)
         self.assertEqual(root.left.val, 5)
         self.assertIsNotNone(root.right)
         self.assertEqual(root.right.val, 15)

        

    def test_insert_duplicate_returns_unchanged_tree(self):
        
        root = Node(10, left = Node(5))

        root = insert(root, 5)

        self.assertIsNone(root.left.left)
        self.assertIsNone(root.left.right)

        pass


class TestDelete(unittest.TestCase):
    def test_delete_leaf_node(self):
        root = Node(20, left = Node(6))

        root = delete(root, 6)

        self.assertIsNone(root.left)


        pass
    def test_delete_node_with_one_child(self):

        root = Node(20, left = Node(10, left = Node(5)) )
        

        root = delete(root, 10)
        self.assertEqual(root.left.val, 5)


        self.assertEqual(root.left.val, 5)


        pass

    def test_delete_node_with_two_children(self):
        root = Node(20, left = Node(10, left=Node(5), right = Node(15))
                    , right = Node(25))

        
        root = delete(root, 10)

        self.assertNotEqual(root.left.val, 10)

        self.assertTrue(root.left.val == 5 or root.left.val == 15  )
        pass

if __name__ == "__main__":
    unittest.main()