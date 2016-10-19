
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 28 12:30:39 2016

@author: ameliawilson
"""


class Node(object):
        
    def __init__(self, data=None, next_node=None, position=0):
        self.data = data
        self.next_node = next_node
        
    def get_data(self):
        return self.data
        
    def get_next(self):
        return self.next_node
        
    def set_next(self, new_next):
        self.next_node = new_next
        



class LinkedList(object):
    
    def __init__(self, head=None):
        self.head = head
        
    def insert(self, data, position=None):
        print("INSERT! | data = "+str(data)+" | pos = "+str(position))
        if position is None:
            new_node = Node(data)
            new_node.set_next(self.head)
            self.head = new_node
        elif position < self.size():
            current = self.head
            previous = None
            count = 0
            while current and count <= position:
                previous = current
                current = current.get_next()
                count += 1
            new_node = Node(data)
            new_node.set_next(current)
            new_node.position = position
            previous.set_next(new_node)
            
        else:
            raise ValueError("Position %d exceeds size of current list" % position)
            
            
    def size(self):
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.get_next()
        return count
    
    def get_position(self, data):
        node = self.get(data)
        if node is not None:
            return node.get_position()
        return None
        
    
    def get(self, data):
        current = self.head
        found = False
        while current and not found:
            if current.get_data() == data:
                found = True
            else:
                current = current.get_next()
        return current
            
    def delete(self, data):
        current = self.head
        previous = None
        found = False
        while current and not found:
            if current.get_data() == data:
                found = True
            else:
                previous = current
                current = current.get_next()
        if current is None:
            raise ValueError("Data not in list")
        if previous is None:
            self.head = current.get_next()
        else:
            previous.set_next(current.get_next())
            
    
            