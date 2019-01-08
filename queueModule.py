'''
Created on Dec 4, 2017

@author: Andrea Graziani - matricola 0189326
@version: 1.0
'''


class Queue():
    """
    THis class represents a 'queue', a First-In-First-Out (FIFO) data structure. 
    In a FIFO data structure, the first element added to the queue will be the first one to be removed.
    """

    def __init__(self):
        """
        Constructs a newly allocated 'Queue' object.
        """
        self._queue = list()

    def enqueue(self, elem):
        """
        Insert specified object into a queue.
        
        @param elem: Represents an object. 
        """
        
        self._queue.append(elem)

    def dequeue(self):
        """
        Retrieve the first object from a queue.
        
        @return: An object stored at top of the queue.
        """
        
        if len(self._queue) == 0:
            return None
        return self._queue.pop(0)
    
    def isEmpty(self):
        """
        Check if a 'Queue' object is empty.
        
        @return: A boolean value: 'True' if queue is empty, otherwise 'False'
        """
        
        return (len(self._queue) == 0)
