# Uzel binárního stromu
class TreeNode:
    def __init__(self, value, left = None, right = None):
        self.left = left
        self.right = right
        self.value = value
     
# binární strom
class BinaryTree:
    def __init__(self, root):
        self.root = root

    # funkce na vypsání všech hodnot ve stromě (jen zabaluje vnitřní rekurzivní funkci)
    def print_tree(self):
        self.__print_subtree_under(self.root)
        print()
    
    # rekurzivní funkce vypisující podstrom pod daným uzlem v preorder notaci
    def __print_subtree_under(self, node):
        if node == None:
            # pokud je uzel None, jen vypíšeme None
            print(None, end=" ")
        else:
            # jinak vypíšeme nejdřív hodnotu uzlu
            print(node.value, end=" ")
            # pak rekurzivně levý podstrom
            self.__print_subtree_under(node.left)
            # a pak rekurzivně pravý podstrom
            self.__print_subtree_under(node.right)

    

# Příklad - sestavení a vypsání stromu
n = TreeNode(3)
n2 = TreeNode(5, n, None)
n3 = TreeNode(7, None, None)
n4 = TreeNode(12, n2, n3)
b = BinaryTree(n4)
b.print_tree()

# Alternativní sestavení ekvivalentního stromu
n4 = TreeNode(12,
        TreeNode(5, 
            TreeNode(3),
            None
        ),
        TreeNode(7)
    )
b = BinaryTree(n4)
b.print_tree()
