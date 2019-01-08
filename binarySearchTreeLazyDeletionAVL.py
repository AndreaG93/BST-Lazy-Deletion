'''
Created on Nov 29, 2017

@author: Andrea Graziani - matricola 0189326
@version: 1.0
'''

from binarySearchTreeNode import binarySearchTreeNodeAVLwithLazyDeletion
from binarySearchTreeAVL import binarySearchTreeAVL


class binarySearchTreeLazyDeletionAVL(binarySearchTreeAVL):
    """
    This class is used to represent a BST AVL with lazy deletion.
    """
    
    def __init__(self, rootNode=None):
        '''
        Constructs a newly allocated 'binarySearchTreeLazyDelectionAVL' object.
        
        @param rootNode: It represents a 'binarySearchTreeNodeAVLwithLazyDeletion' object.
        '''
        binarySearchTreeAVL.__init__(self, rootNode)
    
    def insert(self, key, value):
        """
        This function is used to insert a new (key, value) pair into tree.
        
        @param key: Represents a key.      
        @param value: Represents a value. 
        """
        
        # If tree is empty, newly created node become root...
        # ---------------------------------------------------- #
        if (not self._rootNode):
            self._rootNode = binarySearchTreeNodeAVLwithLazyDeletion(key, value)
            return
        else:
            
            currentNode = self._rootNode
            parentNode = None
            insertToLeft = True
            
            # Search parent of newly created node...
            # ---------------------------------------------------- #
            while (currentNode is not None):
                
                parentNode = currentNode
                
                # Node is not deleted...
                # ---------------------------------------------------- #
                if (currentNode._isValid):
                    
                    # CASE 1:
                    # ---------------------------------------------------- #
                    if (key <= currentNode._key):                
                        currentNode = currentNode._leftSon
                        insertToLeft = True
                        
                    # CASE 2:
                    # ---------------------------------------------------- #
                    else:
                        currentNode = currentNode._rightSon
                        insertToLeft = False
                        
                # Node is deleted...
                # ---------------------------------------------------- #      
                else:   
                    
                    # CASE 1:
                    # ---------------------------------------------------- #
                    if (currentNode.hasRightSon() and (key > currentNode._rightSon._key)):     
                        currentNode = currentNode._rightSon
                        insertToLeft = False
                        
                    # CASE 2:
                    # ---------------------------------------------------- #
                    elif (currentNode.hasLeftSon() and (key < currentNode._leftSon._key)):
                        
                        currentNode = currentNode._leftSon
                        insertToLeft = True
                        
                    # CASE 3:
                    # ---------------------------------------------------- #
                    else:
                        
                        # Copy data into deleted node...
                        # ---------------------------------------------------- #
                        currentNode._isValid = True
                        currentNode._key = key
                        currentNode._value = value
                        return
              
            # Now allocate a new 'binarySearchTreeNodeAVLwithLazyDeletion' object...
            # ---------------------------------------------------- #
            newNode = binarySearchTreeNodeAVLwithLazyDeletion(key, value) 
            
            # Add parent...
            newNode._parent = parentNode 
                          
            # Insert new node...
            # ---------------------------------------------------- #
            if (insertToLeft):      
                parentNode._leftSon = newNode
                newNode._isLeftSon = True
                
            else:
                parentNode._rightSon = newNode
                newNode._isLeftSon = False
                
            # If necessary, update balance factor...
            # ---------------------------------------------------- #
            if (parentNode.hasOnlyOneSon()):
                self._updateNodeSubtreesHeightAlongTree(newNode)
            
    def delete(self, key):
        """
        This function is used to delete first occurrence of a node with specified key from tree.
        
        @param key: Represents a key. 
        @return: A boolean value: 'True' if specified node is correctly deleted, otherwise 'False'.
        """
        
        currentNode = self._rootNode
              
        # Searching...
        # ---------------------------------------------------- #
        while(currentNode):
                
            # CASE 1:
            # ---------------------------------------------------- #
            if (key < currentNode._key):                              
                currentNode = currentNode._leftSon         
            
            # CASE 2:
            # ---------------------------------------------------- #
            elif(key > currentNode._key):           
                currentNode = currentNode._rightSon  
              
            # CASE 3:
            # ---------------------------------------------------- #
            else:  
                if (currentNode._isValid):
                    currentNode._isValid = False
                    return True
                else:
                    currentNode = currentNode._leftSon
                        
        return False
        
    def search(self, key, allowRestructuring):
        """
        This function is used to search first occurrence of a node with specified key into tree.
        
        @param key: Represents a key. 
        @param allowRestructuring: A boolean value used to enable or disable 'tree restructuring'.
        @return: If specified node exists, returns it; otherwise it returns 'None'
        """
         
        # This list object is used to store met invalid nodes...
        invalidNodeList = list()
        currentNode = self._rootNode
              
        # Searching...
        # ---------------------------------------------------- #
        while(currentNode):
              
            # Keeping track invalid nodes...
            if (allowRestructuring and (not currentNode._isValid)):
                invalidNodeList.append(currentNode)
              
            # CASE 1:
            # ---------------------------------------------------- #
            if (key < currentNode._key):                              
                currentNode = currentNode._leftSon         
            
            # CASE 2:
            # ---------------------------------------------------- #
            elif(key > currentNode._key):           
                currentNode = currentNode._rightSon  
              
            # CASE 3:
            # ---------------------------------------------------- #
            else:  
                if (currentNode._isValid):       
                    break
                else:
                    currentNode = currentNode._leftSon
               
        # If requested, delete found invalid nodes physically...
        # ---------------------------------------------------- #
        for item in invalidNodeList:
            self.deleteNode(item)
              
        return currentNode
