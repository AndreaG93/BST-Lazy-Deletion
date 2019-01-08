'''
Created on Dec 5, 2017

@author: Andrea Graziani - matricola 0189326
@version: 1.0
'''

from binarySearchTreeLazyDeletionAVL import binarySearchTreeLazyDeletionAVL

import random
import unittest
import timeit
import functools


class BinarySearchTreeLazyDelectionAVLTest(unittest.TestCase):
    """
    This class is used to test correctness of method decribed into 'BinarySearchTreeLazyDelection' class.
    
    @note: testcase is created by subclassing unittest.TestCase.
    """

    def test_LeftRotation(self):
        """
        This test is used to test 'LeftRotation'.
        """
        
        # Allocate a new 'binarySearchTreeLazyDeletionAVL' object
        # ---------------------------------------------------- #
        myBST = binarySearchTreeLazyDeletionAVL()
        
        # Insert some nodes (with random values)...
        # ---------------------------------------------------- #
        myBST.insert(55, chr(random.randint(65, 122)))
        myBST.insert(44, chr(random.randint(65, 122)))
        myBST.insert(66, chr(random.randint(65, 122)))
        myBST.insert(77, chr(random.randint(65, 122)))
        
        # Inserting following node, tree becomes unbalanced on the right...
        # ---------------------------------------------------- #
        myBST.insert(88, chr(random.randint(65, 122)))
    
        self.assertTrue(myBST.isAVL(), "")
        self.assertEqual(myBST._rootNode._rightSon._key, 77)
        
        # Print for debug...
        myBST.printTree()
        
    def test_rightRotation(self):
        """
        This test is used to test 'rightRotation'.
        """
        
        # Allocate a new 'binarySearchTreeLazyDeletionAVL' object
        # ---------------------------------------------------- #
        myBST = binarySearchTreeLazyDeletionAVL()
        
        # Insert some nodes (with random values)...
        # ---------------------------------------------------- #
        myBST.insert(77, chr(random.randint(65, 122)))
        myBST.insert(88, chr(random.randint(65, 122)))
        myBST.insert(50, chr(random.randint(65, 122)))
        myBST.insert(40, chr(random.randint(65, 122)))
        
        # Inserting following node, tree becomes unbalanced on the right...
        # ---------------------------------------------------- #
        myBST.insert(30, chr(random.randint(65, 122)))
    
        self.assertTrue(myBST.isAVL())
        self.assertEqual(myBST._rootNode._leftSon._key, 40)
        
        # Print for debug...
        myBST.printTree()
        
    def test_LR_Imbalance(self):
        """
        This test is used to test 'LR_Imbalance'.
        """
        
        # Allocate a new 'binarySearchTreeLazyDeletionAVL' object
        # ---------------------------------------------------- #
        myBST = binarySearchTreeLazyDeletionAVL()
        
        # Insert some nodes (with random values)...
        # ---------------------------------------------------- #
        myBST.insert(77, chr(random.randint(65, 122)))
        myBST.insert(88, chr(random.randint(65, 122)))
        myBST.insert(50, chr(random.randint(65, 122)))
        myBST.insert(40, chr(random.randint(65, 122)))
        myBST.insert(30, chr(random.randint(65, 122)))
        
        # Print for debug...
        myBST.printTree()
        
        # Inserting following node, tree have a LR unbalance type...
        # ---------------------------------------------------- #
        myBST.insert(55, chr(random.randint(65, 122)))
        myBST.printTree()
        self.assertTrue(myBST.isAVL())
        self.assertEqual(myBST._rootNode._key, 50)
        
        # Print for debug...
        myBST.printTree()
    
    def test_RL_Imbalance(self):
        """
        This test is used to test 'RL_Imbalance'.
        """
        
        # Allocate a new 'binarySearchTreeLazyDeletionAVL' object
        # ---------------------------------------------------- #
        myBST = binarySearchTreeLazyDeletionAVL()
        
        # Insert some nodes (with random values)...
        # ---------------------------------------------------- #
        myBST.insert(55, chr(random.randint(65, 122)))
        myBST.insert(66, chr(random.randint(65, 122)))
        myBST.insert(40, chr(random.randint(65, 122)))
        myBST.insert(59, chr(random.randint(65, 122)))
        myBST.insert(70, chr(random.randint(65, 122)))
        
        # Inserting following node, tree have a RL unbalance type...
        # ---------------------------------------------------- #
        myBST.insert(58, chr(random.randint(65, 122)))
        self.assertTrue(myBST.isAVL())
        self.assertEqual(myBST._rootNode._key, 59)
        
        # Print for debug...
        myBST.printTree()
    
    def test_insertNodeAfterDeletion(self):
        """
        This test is used to test insertion after a deletion.
        """
    
        # Allocate a new 'binarySearchTreeLazyDeletionAVL' object
        # ---------------------------------------------------- #
        myBST = binarySearchTreeLazyDeletionAVL()
        
        # Insert some nodes (with random values)...
        # ---------------------------------------------------- #
        myBST.insert(23, chr(random.randint(65, 122)))
        myBST.insert(55, chr(random.randint(65, 122)))
        myBST.insert(66, chr(random.randint(65, 122)))
        myBST.insert(87, chr(random.randint(65, 122)))
        myBST.insert(11, chr(random.randint(65, 122)))
        
        print("\nBefore delection")
        # Print for debug...
        myBST.printTree()
        
        # Delete a node...
        self.assertTrue(myBST.delete(23))
        self.assertFalse(myBST.delete(23))
        
        print("\nAfter delection")
        # Print for debug...
        myBST.printTree()
        
        # Inser a node...
        myBST.insert(34, chr(random.randint(65, 122)))
        self.assertEqual(myBST._rootNode._leftSon._key, 34)
    
        print("\nAfter inserction")
        # Print for debug...
        myBST.printTree()
    
    def test_deletion(self):
        """
        This test is used to test deletion.
        """
        
        # Allocate a new 'binarySearchTreeLazyDeletionAVL' object
        # ---------------------------------------------------- #
        myBST = binarySearchTreeLazyDeletionAVL()
        
        # Insert some nodes (with random values)...
        # ---------------------------------------------------- #
        myBST.insert(23, chr(random.randint(65, 122)))
        myBST.insert(55, chr(random.randint(65, 122)))
        myBST.insert(66, chr(random.randint(65, 122)))
        myBST.insert(66, chr(random.randint(65, 122)))
        myBST.insert(11, chr(random.randint(65, 122)))
        
        # Print for debug...
        myBST.printTree()
        
        self.assertTrue(myBST.delete(23))
        self.assertTrue(myBST.delete(11))
        self.assertTrue(myBST.delete(66))
        self.assertTrue(myBST.delete(66))
        self.assertFalse(myBST.delete(66))
        
        self.assertIsNone(myBST.search(11, False))
        self.assertIsNone(myBST.search(23, False))
        self.assertIsNone(myBST.search(66, False))
        
        # Print for debug...
        myBST.printTree()
        
    def test_rootDeletion(self):
        """
        This test is used to test deletion of root node.
        """
        
        # Allocate a new 'binarySearchTreeLazyDeletionAVL' object
        # ---------------------------------------------------- #
        myBST = binarySearchTreeLazyDeletionAVL()
        
        # Insert some nodes (with random values)...
        # ---------------------------------------------------- #
        myBST.insert(23, chr(random.randint(65, 122)))
        myBST.insert(11, chr(random.randint(65, 122)))
        myBST.insert(66, chr(random.randint(65, 122)))
        
        myBST.delete(23)
        myBST.search(11, True)
        myBST.delete(11)
        myBST.search(66, True)
        myBST.delete(66)
        myBST.search(66, True)
        
        # If reached, test OK...
        assert(True)
           
    def test_searchAndAutoRestructuration(self):
        """
        This test is used to test 'Restructuration'.
        """
        
        # Allocate a new 'binarySearchTreeLazyDeletionAVL' object
        # ---------------------------------------------------- #
        myBST = binarySearchTreeLazyDeletionAVL()
        
        # Insert some nodes (with random values)...
        # ---------------------------------------------------- #
        myBST.insert(23, chr(random.randint(65, 122)))
        myBST.insert(55, chr(random.randint(65, 122)))
        myBST.insert(66, chr(random.randint(65, 122)))
        myBST.insert(66, chr(random.randint(65, 122)))
        myBST.insert(11, chr(random.randint(65, 122)))
        
        self.assertTrue(myBST.delete(23))
        
        # Print for debug...
        myBST.printTree()
        
        # Checking 'searching'...
        self.assertIsNone(myBST.search(23, True))
        self.assertIsNotNone(myBST.search(11, True))
        
        # Checking 'restructuration'...
        self.assertEqual(myBST._rootNode._leftSon._key, 11)
        self.assertTrue(myBST.isAVL())
        
        # Print for debug...
        myBST.printTree()
        
    def test_searchAndAutoRestructuration_n1(self):
        """
        This test is used to test 'Restructuration'.
        """
        
        # Allocate a new 'binarySearchTreeLazyDeletionAVL' object
        # ---------------------------------------------------- #
        myBST = binarySearchTreeLazyDeletionAVL()
        
        # Insert some nodes (with random values)...
        # ---------------------------------------------------- #
        myBST.insert(23, chr(random.randint(65, 122)))
        myBST.insert(55, chr(random.randint(65, 122)))
        myBST.insert(66, chr(random.randint(65, 122)))
        myBST.insert(66, chr(random.randint(65, 122)))
        myBST.insert(11, chr(random.randint(65, 122)))
        myBST.insert(25, chr(random.randint(65, 122)))
        myBST.insert(90, chr(random.randint(65, 122)))
        myBST.insert(1, chr(random.randint(65, 122)))
        
        # Delection...
        self.assertTrue(myBST.delete(23))
        
        # Search a node and test restructuration...
        self.assertIsNotNone(myBST.search(1, True))
        self.assertEqual(myBST._rootNode._leftSon._key, 11)
        
        # Print for debug...
        myBST.printTree()
        
    def test_searchAndAutoRestructuration_n2(self):
        """
        This test is used to test 'Restructuration'.
        """
        
        # Allocate a new 'binarySearchTreeLazyDeletionAVL' object
        # ---------------------------------------------------- #
        myBST = binarySearchTreeLazyDeletionAVL()
        
        # Insert some nodes (with random values)...
        # ---------------------------------------------------- #
        myBST.insert(23, chr(random.randint(65, 122)))
        myBST.insert(55, chr(random.randint(65, 122)))
        myBST.insert(66, chr(random.randint(65, 122)))
        myBST.insert(66, chr(random.randint(65, 122)))
        myBST.insert(11, chr(random.randint(65, 122)))
        myBST.insert(25, chr(random.randint(65, 122)))
        myBST.insert(90, chr(random.randint(65, 122)))
        myBST.insert(1, chr(random.randint(65, 122)))
        
        # Delection nodes...
        self.assertTrue(myBST.delete(23))
        self.assertTrue(myBST.delete(11))
        
        # Search a node and test restructuration...
        self.assertIsNotNone(myBST.search(1, True))
        self.assertEqual(myBST._rootNode._leftSon._key, 1)
        
        myBST.printTree()
        
    def test_searchAndAutoRestructuration_n3(self):
        """
        This test is used to test 'Restructuration'.
        """
         
        # Allocate a new 'binarySearchTreeLazyDeletionAVL' object
        # ---------------------------------------------------- #
        myBST = binarySearchTreeLazyDeletionAVL()
        
        # Insert some nodes (with random values)...
        # ---------------------------------------------------- #
        myBST.insert(23, chr(random.randint(65, 122)))
        myBST.insert(55, chr(random.randint(65, 122)))
        myBST.insert(66, chr(random.randint(65, 122)))
        myBST.insert(66, chr(random.randint(65, 122)))
        myBST.insert(11, chr(random.randint(65, 122)))
        myBST.insert(25, chr(random.randint(65, 122)))
        myBST.insert(90, chr(random.randint(65, 122)))
        myBST.insert(1, chr(random.randint(65, 122)))
        
        # Print for debug...
        myBST.printTree()
        
        # Delection nodes...
        self.assertTrue(myBST.delete(66))
        self.assertTrue(myBST.delete(66))
        
        # Search a node and test restructuration...
        self.assertIsNotNone(myBST.search(90, True))
        self.assertEqual(myBST._rootNode._rightSon._key, 66)
        
        # Print for debug...
        myBST.printTree()
        
    def test_timing_1(self):
        """
        This test is used to analyze performance of a BST with lazy deletion.
        """
        
        # Allocate a new 'binarySearchTreeLazyDeletionAVL' object
        # ---------------------------------------------------- #
        myBST = binarySearchTreeLazyDeletionAVL()
 
        def insert(myBST):
            
            # Adding some nodes...
            # ---------------------------------------------------- #  
            for count in range(1, 5000):
                myBST.insert(count, chr(random.randint(65, 122)))
                    
        def delete(myBST):
            
            # delete some nodes...
            # ---------------------------------------------------- #  
            for count in range(1, 5000, 2):    
                myBST.delete(count)
             
        def searchRestructuringNotAllowed(myBST):
              
            # Searching nodes...
            # ---------------------------------------------------- #        
            for count in range(2, 5000, 2):    
                myBST.search(count, False)
                
        def searchRestructuringAllowed(myBST):
           
            # Searching nodes...
            # ---------------------------------------------------- #         
            for count in range(2, 5000, 2):    
                myBST.search(count, True)
              
        def searchRestructuringNotAllowed_n2(myBST):
              
            # Searching nodes...
            # ---------------------------------------------------- #  
            for count in range(2, 5000, 2):    
                myBST.search(count, False)
                    
        print("")
        print("Time to add some nodes:                     %.20f" % min(timeit.Timer(functools.partial(insert, myBST)).repeat(repeat=1, number=1)))
        print("Time to delete some nodes:                  %.20f" % min(timeit.Timer(functools.partial(delete, myBST)).repeat(repeat=1, number=1)))
        print("Time to search node (not Restructuring):    %.20f" % min(timeit.Timer(functools.partial(searchRestructuringNotAllowed, myBST)).repeat(repeat=1, number=1)))
        print("Time to search node (with Restructuring):   %.20f" % min(timeit.Timer(functools.partial(searchRestructuringAllowed, myBST)).repeat(repeat=1, number=1)))
        print("Time to research node (not Restructuring):  %.20f" % min(timeit.Timer(functools.partial(searchRestructuringNotAllowed_n2, myBST)).repeat(repeat=1, number=1)))
               
    def test_timing_2(self):
        """
        This test is used to compare performance between a BST and a BST with lazy deletion: 
        'deletion' version.
        """
        
        # Allocate a new 'binarySearchTreeLazyDeletionAVL' object
        # ---------------------------------------------------- #
        myBST_1 = binarySearchTreeLazyDeletionAVL()
        myBST_2 = binarySearchTreeLazyDeletionAVL()
            
        # Adding some nodes...
        # ---------------------------------------------------- #  
        for count in range(1, 10000):
            # Insert node into tree...
            myBST_1.insert(count, chr(random.randint(65, 122)))
            myBST_2.insert(count, chr(random.randint(65, 122)))
        
        def deleteLazy(myBST_1):
            
            myBST_1.delete(500)
            
        def delete(myBST_2):
            
            myBST_2.deleteNode(myBST_2.search(500, False))
        
        print("")
        print("Time to delete a node:                  %.20f" % min(timeit.Timer(functools.partial(delete, myBST_1)).repeat(repeat=1, number=1)))
        print("Time to delete a node (lazy delection): %.20f" % min(timeit.Timer(functools.partial(deleteLazy, myBST_2)).repeat(repeat=1, number=1)))
        
    def test_timing_3(self):
        """
        This test is used to compare performance between a BST and a BST with lazy deletion: 
        'insertion' version.
        """
        
        # Allocate a new 'binarySearchTreeLazyDeletionAVL' object
        # ---------------------------------------------------- #
        myBST_1 = binarySearchTreeLazyDeletionAVL()
        myBST_2 = binarySearchTreeLazyDeletionAVL()
            
        # Adding some nodes...
        # ---------------------------------------------------- #  
        for count in range(1, 10000):
            # Insert node into tree...
            myBST_1.insert(count, chr(random.randint(65, 122)))
            myBST_2.insert(count, chr(random.randint(65, 122)))
            
        # Delete a node...
        myBST_1.delete(500)
        
        def InsertLazy(myBST_1):
            
            myBST_1.insert(500, chr(random.randint(65, 122)))
            
        def Insert(myBST_2):
            
            myBST_2.insert(500, chr(random.randint(65, 122)))
            
        print("")
        print("Time to insert a node:                  %.20f" % min(timeit.Timer(functools.partial(Insert, myBST_2)).repeat(repeat=1, number=1)))
        print("Time to insert a node (lazy delection): %.20f" % min(timeit.Timer(functools.partial(InsertLazy, myBST_1)).repeat(repeat=1, number=1)))   
        
    def test_timing_4(self):
        """
        This test is used to compare performance between a BST and a BST with lazy deletion: 
        'saerching' version.
        """
        
        # Allocate a new 'binarySearchTreeLazyDeletionAVL' object
        # ---------------------------------------------------- #
        myBST_1 = binarySearchTreeLazyDeletionAVL()
        myBST_2 = binarySearchTreeLazyDeletionAVL()
            
        # Adding some nodes...
        # ---------------------------------------------------- #  
        for count in range(1, 10000):
            # Insert node into tree...
            myBST_1.insert(count, chr(random.randint(65, 122)))
            myBST_2.insert(count, chr(random.randint(65, 122)))
            
        # Deleting nodes...
        # ---------------------------------------------------- #      
        for count in range(1, 10000, 2):
            
            # Insert node into tree...
            myBST_1.deleteNode(myBST_1.search(count, False))
            myBST_2.delete(count)
            
        def Search(myBST):
            
            myBST.search(5000, False)
            
        def SearchLazy(myBST):
            
            myBST.search(5000, False)
            
        print("")
        print("Time to search a node (lazy deletion):  %.20f" % min(timeit.Timer(functools.partial(SearchLazy, myBST_2)).repeat(repeat=1, number=1)))   
        print("Time to search a node:                  %.20f" % min(timeit.Timer(functools.partial(Search, myBST_1)).repeat(repeat=1, number=1)))
        
        
if __name__ == '__main__':
    
    suite = unittest.TestLoader().loadTestsFromTestCase(BinarySearchTreeLazyDelectionAVLTest)
    unittest.TextTestRunner(verbosity=2).run(suite)
    
