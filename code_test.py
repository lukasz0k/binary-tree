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

    def test_short(self):
        code = Code()
        self.assertEqual(code.create_code("d"),
                         LeafNode("d", 1))

    def test_deep_tree_different_start(self):
        code = Code()
        result = code.create_code("deeaaaaaaaaaabbcdddeeeaaaaa")
        self.assertEqual(result,
                         InnerNode(
                             InnerNode(
                                 LeafNode("e", 5),
                                 InnerNode(
                                     InnerNode(
                                         LeafNode("c", 1),
                                        LeafNode("b", 2)
                                        ),
                                     LeafNode("d", 4)
                                 )
                             ),
                             LeafNode("a", 15)
                         )
                         )

    def test_equal_frequency(self):
        """this test showed a method error, when different symbols had the same number of repetitions,
         the solution did not sort them in alphabetical order"""
        code = Code()
        result = code.create_code("dacb")
        self.assertEqual(result,
                         InnerNode(
                             InnerNode(
                                 LeafNode("a", 1),
                                 LeafNode("b", 1)
                             ),
                             InnerNode(
                                 LeafNode("c", 1),
                                 LeafNode("d", 1)
                             )
                         )
                         )

    def test_upper_and_lower(self):
        """this test showed a method error, when the starting text has different symbol sizes"""
        code = Code()
        result = code.create_code("aaAbcaB")
        self.assertEqual(result,
                         InnerNode(
                             InnerNode(
                                 LeafNode("c", 1),
                                 LeafNode("b", 2)
                             ),
                             LeafNode("a", 4)
                         )
                         )

    def test_with_spaces(self):
        """this test showed a method error, when the starting text has spaces"""
        code = Code()
        result = code.create_code("aa bc aba")
        self.assertEqual(result,
                         InnerNode(
                             InnerNode(
                                 LeafNode("c", 1),
                                 LeafNode("b", 2)
                             ),
                             LeafNode("a", 4)
                         )
                         )
