import unittest

from code import Code
from tree import LeafNode, InnerNode


class CodeTest(unittest.TestCase):
    def test_one_letter(self):
        code = Code()
        self.assertEqual(code.create_code("aaaaa"), LeafNode("a", 5))

    def test_two_letters(self):
        code = Code()
        self.assertEqual(code.create_code("aab"),
                         InnerNode(
                             LeafNode("b", 1),
                             LeafNode("a", 2)
                         ))

    def test_multi_letter_string(self):
        code = Code()
        self.assertEqual(code.create_code("aabcbacbacaba"),
                         InnerNode(
                             LeafNode("a", 6),
                             InnerNode(
                                 LeafNode("c", 3),
                                 LeafNode("b", 4)
                             )
                         ))

    def test_deep_tree(self):
        code = Code()
        result = code.create_code("aaaaaaaaaaaaabccddddeeeee")
        self.assertEqual(result,
                         InnerNode(
                             InnerNode(
                                 LeafNode("e", 5),
                                 InnerNode(
                                     InnerNode(
                                        LeafNode("b", 1),
                                        LeafNode("c", 2)
                                        ),
                                     LeafNode("d", 4)
                                 )
                             ),
                             LeafNode("a", 13)
                         )
                         )
