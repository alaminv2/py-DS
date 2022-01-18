from collections import deque


# General tree
class TreeNode:
    def __init__(self, name=None, designation=None, parent=None):
        self.name = name
        self.designation = designation
        self.parent = parent
        self.children = []

    def add_child(self, name=None, designation=None, parent=None):
        child = TreeNode(name, designation, self)
        self.children.append(child)
        return child

    def print_tree(self, level=0):
        lvl = self.get_level()
        if lvl <= level:
            prefix = ' ' * lvl * 2
            prefix += '|__' if self.parent else ''
            print(f'{prefix}{self.name} ({self.designation})')
            if self.children:
                for child in self.children:
                    child.print_tree(level)

    def get_level(self):
        level = 0
        parent = self.parent
        while parent:
            level += 1
            parent = parent.parent
        return level

    def __str__(self):
        return f'{self.name}, {self.designation}'


# Binary tree
class BinaryTree:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None

    def add_child(self, data):
        pass

    def level_order_print(self):
        # Method using queue
        queue = deque()
        result = list()
        queue.append(self)
        while queue:
            cur = queue.popleft()
            if cur.left:
                queue.append(cur.left)
            if cur.right:
                queue.append(cur.right)
            result.append(cur.data)
        return result

    def insert_level_order(self, data):
        queue = deque()
        queue.append(self)
        while queue:
            cur = queue.popleft()
            if not cur.left:
                cur.left = BinaryTree(data)
                break
            else:
                queue.append(cur.left)

            if not cur.right:
                cur.right = BinaryTree(data)
                break
            else:
                queue.append(cur.right)

        # ---Method using level
        # ---get the height of tree
        # ---iterate over height and print all nodes of that level
        # height = self.get_tree_height()
        # for i in range(1, height+1):
        #     self.print_current_level(i)

    def delete_node(self, key):
        if not self:
            return
        queue = list()
        queue.append(self)
        while queue:
            pass

    # Level order tree traversal
    def get_tree_height(self):
        l_height = 0 if not self.left else self.left.get_tree_height()
        r_height = 0 if not self.right else self.right.get_tree_height()

        if l_height > r_height:
            return l_height + 1
        else:
            return r_height + 1

    def __str__(self):
        return str(self.data)


if __name__ == '__main__':
    parent = BinaryTree(10)
    parent.left = BinaryTree(11)
    parent.right = BinaryTree(9)
    parent.left.left = BinaryTree(7)
    parent.right.left = BinaryTree(15)
    parent.right.right = BinaryTree(8)

    parent.insert_level_order(12)
    print(parent.level_order_print())

    parent.delete_node(12)

