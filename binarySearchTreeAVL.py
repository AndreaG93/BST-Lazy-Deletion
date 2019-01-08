'''
Created on Dec 4, 2017

@author: Andrea Graziani - matricola 0189326
@version: 1.0
'''

from queueModule import Queue


class binarySearchTreeAVL(object):
    '''
    This class is used to to represent a BST AVL.
    '''
    
    def __init__(self, rootNode=None):
        '''
        Constructs a newly allocated 'binarySearchTreeAVL' object.
        
        @param rootNode: It represents a 'binarySearchTreeAVL' object.
        '''
        
        self._rootNode = rootNode
        
    @staticmethod
    def __cutTreeByLeft(parentNode):
        """
        This function is used to retrieve left subtree of a specified 'BinarySearchTreeNode'; That subtree 
        will be removed from original tree.
        
        @param parentNode: Represents a 'BinarySearchTreeNode' object.
        @return: A 'BinarySearchTree' object.
        """
        
        if (parentNode._leftSon is None):
            return None
        else:
            newBSTRootNode = parentNode._leftSon
            newBST = binarySearchTreeAVL(newBSTRootNode)
            
            # Update attributes
            newBSTRootNode._parent = None
            parentNode._leftSon = None
            
            return newBST
    
    @staticmethod
    def __cutTreeByRight(parentNode):
        """
        This function is used to retrieve right subtree of a specified 'BinarySearchTreeNode'; That subtree 
        will be removed from original tree.
        
        @param parentNode: Represents a 'BinarySearchTreeNode' object.
        @return: A 'BinarySearchTree' object.
        """
        
        if (parentNode._rightSon is None):
            return None
        else:
            newBSTRootNode = parentNode._rightSon
            newBST = binarySearchTreeAVL(newBSTRootNode)
            
            # Update attributes
            newBSTRootNode._parent = None
            parentNode._rightSon = None
            
            return newBST  
    
    def __leftRotation(self, node):
        """
        This function is used to do a simple left rotation.
        
        @param node: Represents a 'BinarySearchTreeNode' object.
        """
     
        # Get 'rightSon' of specified node...
        # ---------------------------------------------------- #
        rightSonNode = node._rightSon  
        parentNode = node._parent  
        
        # Getting necessary subtree...
        # ---------------------------------------------------- #
        leftSubtreeOfRightSon = binarySearchTreeAVL.__cutTreeByLeft(rightSonNode)
            
        # Update tree   
        # ---------------------------------------------------- #
        
        # 1 - ParentNode
        if (parentNode is not None):
           
            if (node._isLeftSon):
                parentNode._leftSon = rightSonNode
                rightSonNode._isLeftSon = True
            else:
                parentNode._rightSon = rightSonNode
                rightSonNode._isLeftSon = False
        else:
            self._rootNode = rightSonNode
        
        # 2 - Node
        if (leftSubtreeOfRightSon is not None):
            
            supportNode = leftSubtreeOfRightSon._rootNode
            node._rightSon = supportNode
            
            supportNode._parent = node
            supportNode._isLeftSon = False
             
        else:
            node._rightSon = None
            
        node._parent = rightSonNode
        node._isLeftSon = True
        
        # 3 - RightSon
        rightSonNode._parent = parentNode
        rightSonNode._leftSon = node
              
    def __rightRotation(self, node):
        """
        This function is used to do a simple right rotation.
        
        @param node: Represents a 'BinarySearchTreeNode' object.
        """
        
        # Get 'rightSon' of specified node...
        # ---------------------------------------------------- #
        leftSonNode = node._leftSon  
        parentNode = node._parent  
        
        # Getting necessary subtree...
        # ---------------------------------------------------- #
        rightSubtreeOfLeftSon = binarySearchTreeAVL.__cutTreeByRight(leftSonNode)
            
        # Update tree   
        # ---------------------------------------------------- #
        
        # 1 - ParetnNode
        if(parentNode is not None):
           
            if (node._isLeftSon):
                parentNode._leftSon = leftSonNode
                leftSonNode._isLeftSon = True
            else:
                parentNode._rightSon = leftSonNode
                leftSonNode._isLeftSon = False
        else:
            self._rootNode = leftSonNode
        
        # 2 - Node
        if (rightSubtreeOfLeftSon is not None):
            
            supportNode = rightSubtreeOfLeftSon._rootNode
            node._leftSon = supportNode
            supportNode._parent = node
            supportNode._isLeftSon = True
            
        else:
            node._leftSon = None
        
        node._parent = leftSonNode
        node._isLeftSon = False
   
        # 3 - RightSon
        leftSonNode._parent = parentNode  
        leftSonNode._rightSon = node
        
    def __rotation(self, node):   
        """
        This function is used to balance a specified node.
        
        @param node: Represents a 'BinarySearchTreeNode' object.
        """
     
        balanceFactor = node.getBalanceFactor()
 
        # CASE 1
        # LEFT subtree is higher by 2 than RIGHT subtree
        # ---------------------------------------------------- #
        if (balanceFactor == 2):
            
            # LL imbalance
            # ---------------------------------------------------- #
            if (node._leftSon.getBalanceFactor() >= 0):
                self.__rightRotation(node) 
                self._updateNodeSubtreesHeightAlongTree(node)     
            
            # LR imbalance
            # ---------------------------------------------------- #
            else:   
                x = node._leftSon
                y = node
                   
                self.__leftRotation(node._leftSon)
                self.__rightRotation(node)
                
                y.updateSubTreesHeight()     
                self._updateNodeSubtreesHeightAlongTree(x)
            
        # CASE 2
        # RIGHT subtree is higher by 2 than LEFT subtree
        # ---------------------------------------------------- #
        elif (balanceFactor == -2):
            
            # RR imbalance
            # ---------------------------------------------------- #
            if (node._rightSon.getBalanceFactor() <= 0):
                self.__leftRotation(node)
                self._updateNodeSubtreesHeightAlongTree(node)
            
            # RL imbalance
            # ---------------------------------------------------- # 
            else:
                x = node._rightSon
                y = node
                
                self.__rightRotation(node._rightSon)
                self.__leftRotation(node)
                
                y.updateSubTreesHeight()   
                self._updateNodeSubtreesHeightAlongTree(x)
  
    def _updateNodeSubtreesHeightAlongTree(self, node):
        """
        This function is used to update subtrees height from a specified node to root node
        
        @param node: Represents a 'BinarySearchTreeNode' object.
        """
        currentNode = node
        
        while(currentNode is not None):
            
            # Update heights...
            # ---------------------------------------------------- #
            currentNode.updateSubTreesHeight()
             
            # Stop the height update at the first unbalanced node....
            # ---------------------------------------------------- #
            if (abs(currentNode.getBalanceFactor()) > 1):
                self.__rotation(currentNode)
                    
            currentNode = currentNode._parent

    def isAVL(self):
        """
        This test-function is used to check if current BST is AVL using breadth-first search (BFS) algorithm.
        @see: 'https://en.wikipedia.org/wiki/Breadth-first_search'
        """
        
        myQueue = Queue()
    
        myQueue.enqueue(self._rootNode)
    
        while(not myQueue.isEmpty()):
            currentNode = myQueue.dequeue()
            
            if (currentNode is not None):

                # Check balance factor...
                # ---------------------------------------------------- #
                if (abs(currentNode.getBalanceFactor()) > 1):
                    return False
                
                myQueue.enqueue(currentNode._leftSon)
                myQueue.enqueue(currentNode._rightSon)
        
        return True
    
    def deleteNode(self, node):
        """
        This function is used to delete specified node physically.
        
        @param node: It represents a "binarySearchTreeNodeAVL" object.
        """
         
        parentNode = node._parent
        son = None
            
        # If a node doesn't have sons...
        # ---------------------------------------------------- #
        if ((not node.hasLeftSon()) and (not node.hasRightSon())):
             
            if (parentNode):    
                if (node._isLeftSon):
                    parentNode._leftSon = None            
                else:
                    parentNode._rightSon = None
            else:
                self._rootNode = None
                return
                            
            self._updateNodeSubtreesHeightAlongTree(parentNode)
              
        # If a node has a only one son (left son)...
        # ---------------------------------------------------- #              
        elif (node.hasOnlyOneSon()):
                   
            son = (node._leftSon if node.hasLeftSon() else node._rightSon)
              
            if (parentNode):
                if (node._isLeftSon):
                    parentNode._leftSon = son  
                    son._isLeftSon = True          
                else:
                    parentNode._rightSon = son
                    son._isLeftSon = False 
            else:
                self._rootNode = son
                
            son._parent = parentNode
         
            self._updateNodeSubtreesHeightAlongTree(parentNode)
                                
        # If an invalid node has a left son and hasn't a right son...
        # ---------------------------------------------------- #              
        elif (node.hasTwoSons()):
            
            # Calc pred...
            # ---------------------------------------------------- #             
            predNode = node._leftSon
                
            while (predNode._rightSon is not None):
                predNode = predNode._rightSon
                
            # Get parent of pred node...    
            predNodeParent = predNode._parent
            
            # swap pred with currentNode
            # ---------------------------------------------------- #          
            
            # Update parent of node to be deleted...
            if (parentNode):
                if (node._isLeftSon):
                    parentNode._leftSon = predNode
                else:
                    parentNode._rightSon = predNode
            else:
                self._rootNode = predNode
                
            # Update 'predNodeParent' parent...
            if (predNode._isLeftSon):
                predNodeParent._leftSon = node
                node._parent = predNodeParent
            else:
                predNodeParent._rightSon = node
                node._parent = predNodeParent
                
            # Update 'node' sons...
            node._rightSon._parent = predNode
            node._leftSon._parent = predNode
            
            # Update 'predNode' sons... 
            if(predNode.hasLeftSon()):
                predNode._leftSon._parent = node
                
            predNode._parent = parentNode
                 
            node._isLeftSon, predNode._isLeftSon = predNode._isLeftSon, node._isLeftSon
            node._leftSon, predNode._leftSon = predNode._leftSon, node._leftSon
            node._rightSon, predNode._rightSon = predNode._rightSon, node._rightSon
            
            # Delete node
            self.deleteNode(node)
            self._updateNodeSubtreesHeightAlongTree(predNode)
    
    def printTree(self):
        """
        This function is used to print a tree using breadth-first search (BFS) algorithm.
        @see: 'https://en.wikipedia.org/wiki/Breadth-first_search'
        """
             
        print("\n\n{0}".format("-"*70))
        print("%-3s | %-15s | %-7s | %-3s | %-3s | %-3s" % ("Key", "Value", "Parent (Att)", "HS", "HD", "Balance Factor"))
        print("{0}".format("-"*70))
        myQueue = Queue()
    
        myQueue.enqueue(self._rootNode)
    
        while(not myQueue.isEmpty()):
            currentNode = myQueue.dequeue()
            if (currentNode is not None):

                print("%-3s | %-15s | %-7s %-4s | %-3s | %-3s | %-3s " % (currentNode._key, currentNode._value if currentNode._isValid else "** Deleted **", currentNode._parent._key if currentNode._parent is not None else "Root", "-" if currentNode._parent is None else "L" if currentNode._isLeftSon else "R", currentNode._leftSubtreeHeight, currentNode._rightSubtreeHeight, currentNode.getBalanceFactor()))
                
                myQueue.enqueue(currentNode._leftSon)
                myQueue.enqueue(currentNode._rightSon)
        
        print("{0}".format("-"*70))
