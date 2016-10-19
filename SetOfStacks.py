from MyStack import StackNode
from MyStack import Stack
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  7 18:14:26 2016

@author: ameliawilson
"""

class SetOfStacksNode(StackNode):
    
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node
                
        
        

class SetOfStacks(Stack):
    
    def __init__(self, top=None, capacity=5):
        self.top = top 
        self.stacks = [] #list of stacks
        self.capacity = capacity #default to 5 items per stack, can input different number
        self.size = 0
        
    def get_last_stack(self):
        if len(self.stacks) == 0:
            return None
        last_stack = self.stacks[len(self.stacks)-1]
        return last_stack
        
        
    def push(self, data):
        new_node = SetOfStacksNode(data)
        new_node.set_next(self.top)
        self.top = new_node
        if len(self.stacks) == 0:
            new_stack = []
            new_stack.append(new_node)
            self.stacks.append(new_stack)
        else:
            last_stack = self.get_last_stack()
            if len(last_stack) < self.capacity:
                last_stack.append(new_node)
            else:
                new_stack = []
                new_stack.append(new_node)
                self.stacks.append(new_stack)
        self.size += 1
    
    def pop(self):
        last_stack = self.get_last_stack() #the top should be in here
        if last_stack is None or len(last_stack) == 0:
            return None
        item = last_stack[len(last_stack)-1]
        last_stack.remove(item)
        if len(last_stack) == 0:
            self.stacks.remove(last_stack)            
        self.top = item.get_next()
        self.size -= 1
        return item
        
        
        
        
        
        
        
    