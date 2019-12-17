# coding=utf-8

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class Tree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if not self.root:
            self.root = Node(key)
        else:
            prev = None
            current = self.root
            while current:
                if current.value != key:
                    prev = current
                    if current.value > key:
                        current = current.right
                    else:
                        current = current.left
            if prev.value > key:
                prev.right = Node(key)
            elif prev.value < key:
                prev.left = Node(key)

    def __contains__(self, key):
        if not self.root:
            return False
        else:
            current = self.root
            while current:
                if current.value == key:
                    return True
                elif current.value > key:
                    current = current.right
                else:
                    current = current.left
            return False    
            
    
    
if __name__ == '__main__':
    t = Tree()
    t.insert(12)
    t.insert(15)
    t.insert(1)
    if 1 in t:
        print("1 in tree")