# -*- coding: utf-8 -*-
"""
Created on Wed Sep 28 23:09:05 2016

@author: ameliawilson
"""

'''
STACKS 
Good for some recursive algorithms: 
 (1) push temp data onto stack and then remove it as you backtrack because the recursive check failed
 (2) implement a recurisve alorithm iteratively 
Can be implemented with a LinkedList as long as items are added/removed from SAME side
'''


class StackNode(object):

    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node

    def get_data(self):
        return self.data
        
    def get_next(self):
        return self.next_node
        
    def set_next(self, new_next):
        self.next_node = new_next
        
class Stack(object):
    
    def __init__(self, top=None):
        self.top = top
        
    def pop(self):
        if self.top is None:
            return None
        item = self.top
        self.top = item.get_next()
        return item      
        
    def push(self, data):
        new_node = StackNode(data)
        new_node.set_next(self.top)
        self.top = new_node
        
    def peek(self):
       if self.top is None:
           raise ValueError("Stack is empty")
       return self.top.get_data()
       
    def is_empty(self):
        return self.top is None
    