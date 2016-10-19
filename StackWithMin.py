from MyStack import StackNode
from MyStack import Stack

# -*- coding: utf-8 -*-
"""
Created on Thu Sep 29 00:56:01 2016

@author: ameliawilson
"""


###############################################################################
# (2) Stack Min: How would you design a stack which , in addition to push &   #
#     pop, has a function min which return the mimum element? push, pop, min  #
#     should all operate in O(1) time.                                        #
###############################################################################

class StackNodeWithMin(StackNode):

    #overwrite __init__ to include minimum
    def __init__(self, data=None, next_node=None, minimum=None):
        self.data = data
        self.next_node = next_node
        self.minimum = minimum        
        
    #add new functions for minimum:
    def get_min(self):
        return self.minimum

    def set_min(self, data):
        self.minimum = min(data, self.minimum)

class StackWithMin(Stack):
       
    #overwrite push to include minimum
    def push(self, data):
        new_node = StackNodeWithMin(data)
        new_node.set_next(self.top)
        new_node.set_min(data) 
        self.top = new_node
 