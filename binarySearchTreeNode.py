'''
Created on Dec 1, 2017

@author: Andrea Graziani - matricola 0189326
@version: 1.0
'''


class binarySearchTreeNode(object):
    '''
    This class represents a node of a binary search tree.
    '''
    
    def __init__(self, key, value):
        '''
        Constructs a newly allocated 'BinarySearchTreeNode' object.
        
        @param key: Represents a key.      
        @param value: Represents a value. 
        '''
        
        self._key = key
        self._value = value  
        
        self._parent = None
        self._leftSon = None
        self._rightSon = None  
    
        # This attribute specifies if current node is a left or right son of his parent...
        self._isLeftSon = False
        
    def hasRightSon(self):
        """
        This function is used to check if current node has a right son.
        
        @return: It returns 'True' if current node has a right child, otherwise it returns 'False'.
        """
        
        return self._rightSon is not None
    
    def hasLeftSon(self):
        """
        This function is used to check if current node has a left son.
        
        @return: It returns 'True' if current node has a left child, otherwise it returns 'False'.
        """
        
        return self._leftSon is not None
    
    def hasOnlyOneSon(self):
        """
        This function is used to check if current node has only one son.
        
        @return: It returns 'True' if current node has only one son, otherwise it returns 'False'.
        """
        
        return ((self._leftSon is not None and self._rightSon is None) or (self._leftSon is None and self._rightSon is not None))

    def hasTwoSons(self):
        """
        This function is used to check if current node has two sons.
        
        @return: It returns 'True' if current node has two sons, otherwise it returns 'False'.
        """
        
        return self._leftSon is not None and self._rightSon is not None 
    
    
class binarySearchTreeNodeAVL(binarySearchTreeNode):   
    '''
    This class represents a node of a binary search tree AVL.
    '''
    
    def __init__(self, key, value):
        '''
        Constructs a newly allocated 'BinarySearchTreeNode' object.
        
        @param key: Represents a key.      
        @param value: Represents a value. 
        '''
        binarySearchTreeNode.__init__(self, key, value)
        
        # Heights of left and right subtree...
        self._leftSubtreeHeight = 0 
        self._rightSubtreeHeight = 0
        
    def getBalanceFactor(self):
        """
        This function is used to calc 'balance factor' of current node.
        
        @return: 'balance factor' of a node.
        """
        
        return (self._leftSubtreeHeight - self._rightSubtreeHeight)
    
    def updateSubTreesHeight(self):
        """
        This function is used to update subtrees height of current node.
        """
        
        # Get sons...
        # ---------------------------------------------------- #
        nodeLeftSon = self._leftSon
        nodeRightSon = self._rightSon
        
        # Calc left subtree height...
        # ---------------------------------------------------- #
        if(nodeLeftSon is not None):
            self._leftSubtreeHeight = max(nodeLeftSon._leftSubtreeHeight, nodeLeftSon._rightSubtreeHeight) + 1
        else:
            self._leftSubtreeHeight = 0
            
        # Calc right subtree height...
        # ---------------------------------------------------- #
        if(nodeRightSon is not None):
            self._rightSubtreeHeight = max(nodeRightSon._leftSubtreeHeight, nodeRightSon._rightSubtreeHeight) + 1
        else:
            self._rightSubtreeHeight = 0


class binarySearchTreeNodeAVLwithLazyDeletion(binarySearchTreeNodeAVL):
    '''
    This class represents a node of a binary search tree AVL with 'lazy deletion'.
    '''

    def __init__(self, key, value):
        
        binarySearchTreeNodeAVL.__init__(self, key, value)
        
        # This attribute is a flag used to mark current node as deleted or not ...
        self._isValid = True
    
            
