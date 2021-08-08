from tree import Node, LeafNode, InnerNode
"""import the rest of classes"""

class Code:
    """
        Your task is to encode the alphabet as a binary tree using the frequencies of letters in the given text. You need to perform
        the following steps

        * for each character in the text calculate its number of occurences / frequency, e.g. for string `aba` it would be `a -> 2`, `b -> 1`
        * for each character and its frequency create a one-node tree
        * take two trees `T1` and `T2` with lowest frequencies and merge them into a larger tree `T1-2` (`T1` should become the left sub-tree and `T2` the right subtree)
        * repeat the previous step until there is only 1 tree left

        That last tree represents the created encoding.
        For example, given text `abaca` you should get:

        ```
              a+b+c(5)
               /  \
              /    \
             /      \
            /        \
          b+c(2)     a(3)
          /   \
         /     \
        b(1)   c(1)
        ```

        All the auxiliary classes for building the tree are provided (see tree.py).
    """

    """first solution"""
    def create_code(self, text: str) -> Node:
        prepared_text = text.lower().replace(" ", "")
        freq = {}
        """make a dictionary with symbol and frequency"""
        for symbol in prepared_text:
            freq[symbol] = prepared_text.count(symbol)

        """create the list that contains symbols and count of theirs occurrences"""
        sorted_freq = {key: value for key, value in sorted(freq.items())}
        nodes = [LeafNode(symbol, frequency) for symbol, frequency in sorted_freq.items()]
        nodes.sort(key=lambda x: x.frequency, reverse=False)

        while len(nodes) > 1:
            """take two with lowest frequency, get rid of them too"""
            node1 = nodes.pop(0)  # [0].copy()
            node2 = nodes.pop(0)  # .copy()
            """merge that"""
            new_node = InnerNode(node1, node2)
            """joined node goes back"""
            nodes.append(new_node)
            """get them sorted again"""
            nodes.sort(key=lambda x: x.frequency, reverse=False)

        return nodes[0]