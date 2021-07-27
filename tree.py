class Node:
    def __init__(self, frequency: int):
        self.frequency = frequency

    def __eq__(self, other):
        return self.frequency == other.frequency

    def __lt__(self, other):
        return self.frequency < other.frequency

    def __gt__(self, other):
        return self.frequency > other.frequency

    def __ge__(self, other):
        return self.frequency >= other.frequency

    def __le(self, other):
        return self.frequency <= other.frequency


class LeafNode(Node):
    def __init__(self, symbol: str, frequency: int):
        super(LeafNode, self).__init__(frequency)
        self.symbol = symbol

    def __str__(self):
        return "symbol: %s, frequency: %s" % (self.symbol, self.frequency)

    def __eq__(self, other):
        return isinstance(other, LeafNode) and self.symbol == other.symbol and self.frequency == other.frequency


class InnerNode(Node):
    def __init__(self, left: Node, right: Node) -> ():
        super(InnerNode, self).__init__(left.frequency + right.frequency)
        self.left = left
        self.right = right

    def __str__(self):
        return "frequency: %s (left: %s), (right: %s)" % (self.frequency, str(self.left), str(self.right))

    def __eq__(self, other):
        return isinstance(other, InnerNode) and self.frequency == other.frequency and self.left == other.left \
               and self.right == other.right
