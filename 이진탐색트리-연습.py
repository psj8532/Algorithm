class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

class BinarySearchTree(object):
    def __init__(self):
        self.root = None

    def set_root(self,data):
        self.root = Node(data)

    def insert(self,data):
        if self.root is None:
            self.set_root(data)
        else:
            self.insert_value(self.root,data)

    def insert_value(self,cur,data):
        if data < cur.data:
            if cur.left is None:
                cur.left = Node(data)
            else:
                self.insert_value(cur.left,data)
        else:
            if cur.right is None:
                cur.right = Node(data)
            else:
                self.insert_value(cur.right,data)

    def find(self,data):
        if self.root is None:
            return False
        else:
            return self.find_value(self.root,data)

    def find_value(self,cur,data):
        if cur is None:
            return False
        if data == cur.data:
            return True
        elif data < cur.data:
            return self.find_value(cur.left,data)
        else:
            return self.find_value(cur.right,data)

    def remove(self,data):
        if self.root is None:
            print('트리가 비어있습니다.')
        else:
            self.remove_value(self.root,data)

    def remove_value(self,cur,data):
        print(cur.data)
        if cur is None:
            return None
        elif data == cur.data:
            if cur.left is None and cur.right is None:
                return None
            elif cur.left is not None and cur.right is None:
                return cur.left
            elif cur.left is None and cur.right is not None:
                return cur.right
            else:
                min_value = self.successor_value(cur.right)
                cur.data = min_value.data
                self.remove_value(cur.right,min_value.data)
                return cur
        elif data < cur.data:
            cur.left = self.remove_value(cur.left,data)
        else:
            cur.right = self.remove_value(cur.right,data)
        return cur

    def successor_value(self,cur):
        while cur.left is not None:
            cur = cur.left
        return cur


arr = [40,10,20,60,15,80,55,70,5]
bst = BinarySearchTree()
for val in arr:
    bst.insert(val)
bst.remove(80)
print(1)