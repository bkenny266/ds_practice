class PyTree(object):

    def __init__(self):
        self.root = None

    def insert(self, node):
        if self.root:
            key_in = node.key
            parent = self.root
            current = self.root

            while True:
                parent = current
                if key_in < current.key:
                    current = current.leftChild
                    if not current:
                        parent.leftChild = node
                        return
                elif key_in > current.key:
                    current = current.rightChild
                    if not current:
                        parent.rightChild = node
                        return
                else:
                    print "Cannot add an item that already exists"
                    return
        else:
            self.root = node


    def find(self, key):
        current = self.root
        while current != None:
            if current.key == key:
                return current.key
            elif key < current.key:
                current = current.leftChild
            elif key > current.key:
                current = current.rightChild

        return None

    def delete(self, key):
        pass

    def traverse(self):
        self._traverse(self.root)

    def _traverse(self, node):
        if node:
            self._traverse(node.leftChild)
            print node.key
            self._traverse(node.rightChild)





class Node(object):

    def __init__(self, key, data):
        self.key = key
        self.data = data
        self.root = False
        self.leftChild = None
        self.rightChild =None






if __name__ == '__main__':
    tree = PyTree()

    input = 1
    while input > 0:
        print "Enter value:",
        input = int(raw_input())
        tree.insert(Node(input, "x"))

    tree.traverse()

    input = 1
    while input > 0:
        print "Find key:",
        input = int(raw_input())
        print tree.find(input)


    tree.traverse()

