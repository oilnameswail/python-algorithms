# -*- coding: utf-8 -*-
"""
Created on Wed Sep 28 23:27:24 2016

@author: ameliawilson
"""

'''
QUEUES - FIFO ordering; items are removed in the same order that they were added
Good for 
 (1) breadth-first search
 (2) implementing a cache
Can be implemented with a LinkedList as long as items are added/removed from OPPOSITE sides
'''


class QueueNode(object):

    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node

    def get_data(self):
        return self.data
        
    def get_next(self):
        return self.next_node
        
    def set_next(self, new_next):
        self.next_node = new_next
        
class Queue(object):
    
    def __init__(self, first=None, last=None):
        self.first = first
        self.last = last
        
    #aka remove: first in first out!
    def dequeue(self):
        if self.first is None:
            raise ValueError("None such element to remove")
        data = self.first.get_data()
        self.first = self.first.get_next()
        if self.first is None:
            self.last = None
        return data
    
    #aka add: add to end, make current end have new end as next
    def enqueue(self, data):
        new_node = QueueNode(data)
        if self.last is not None:
            self.last.set_next(new_node)
        self.last = new_node
        if self.first is None:
            self.first = self.last
            
    def peek(self):
       if self.first is None:
           raise ValueError("Queue is empty")
       return self.first.get_data()
       
    def is_empty(self):
        return self.first is None
    
    def size(self):
        size = 0
        if self.first is None:
            return size
        current = self.first
        while current:
            size+=1
            current = current.get_next()
        return size
            
    