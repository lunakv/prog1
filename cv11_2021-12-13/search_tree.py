class TreeNode:
    '''Uzel binárního stromu'''

    def __init__(self, value, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right

class BinarySearchTree:
    '''Binární vyhledávácí strom'''

    def __init__(self, initial_values = []):
        self.root = None
        for item in initial_values:
            self.insert(item);

    def find(self, value):
        '''Vrátí True, pokud hodnota existuje ve stromě'''
        return self.__find(value, self.root)
    
    def insert(self, value):
        '''Přidá hodnotu do stromu, pokud ještě neexistuje'''
        if self.root is None:
            self.root = TreeNode(value)
        else:
            self.__insert(value, self.root)

    def delete(self, value):
        '''Smaže hodnotu ze stromu (pokud existuje)'''
        raise NotImplementedError

    def pretty_print(self):
        '''Vypíše hezky obsah stromu'''
        self.__print_tabulated(self.root, 0)


    ### Interní rekurzivní funkce
    def __find(self, value, node):
        if node is None:
            return False
        
        if value == node.value:
            return True
        elif value < node.value:
            return self.__find(value, node.left)
        else:
            return self.__find(value, node.right)
    
    def __insert(self, value, node):        
        if value == node.value:
            return
        elif value < node.value:
            if node.left is None:
                node.left = TreeNode(value)
            else:
                self.__insert(value, node.left)
        else:
            if node.right is None:
                node.right = TreeNode(value)
            else:
                self.__insert(value, node.right)
    
    def __print_tabulated(self, node, level):
        print('\t'*level, end='')
        if node is None:
            print('None')
        else:
            print('Node(',node.value,')', sep='')
            self.__print_tabulated(node.left, level+1)
            self.__print_tabulated(node.right, level+1)



# Příklad použití
b = BinarySearchTree([5, 3, 1, 8, 6, 12])
b.pretty_print()
b.insert(8)
b.insert(2)
print('Is 1 in the tree?', b.find(1))
print('Is 2 in the tree?', b.find(2))
print('Is 4 in the tree?', b.find(4))
b.delete(2)
print('Is 2 in the tree?', b.find(2))
