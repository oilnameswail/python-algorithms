from MyQueue import Queue
from MyQueue import QueueNode

# -*- coding: utf-8 -*-
"""
Created on Thu Sep 29 01:14:42 2016

@author: ameliawilson
"""

class BinaryTreeNode(object):

    def __init__(self, value, compare=None):
        self.value = value
        # if a tree lacks a parent, it must be the root        
        self.parent = None
        # children
        self.right = None
        self.left = None
    
class BinarySearchTree(object):
    
    def __init__(self):    
        # classically, binary *search* trees have 'bigger on right' at each node
        self.compare = lambda x,y: -1 if x<y else 1 if x>y else 0
        self.root = None

    def get_root(self):
        return self.root
        
    
    def add(self, new_value):
        #if first node:
        if self.root is None:
            new_node = BinaryTreeNode(new_value)
            self.root = new_node
        else:
            self._add(new_value, self.root)
    
    def _add(self, new_value, node):
        if self.compare(new_value, node.value) < 0:
            if node.left is not None:
                self._add(new_value, node.left)
            else:
                new_node = BinaryTreeNode(new_value)
                new_node.parent = node
                node.left = new_node
                
        else:
            if node.right is not None:
                self._add(new_value, node.right)
            else:
                new_node = BinaryTreeNode(new_value)
                new_node.parent = node
                node.right = new_node
        
    def depth_search(self, value):
        if value is None:
            raise ValueError("Cannot search for null value")
        if self.root is not None:
            visited = {}
            return self._depth_search(value, self.root, visited)
        else: #empty tree
            return None
      
            
    def _depth_search(self, value, node, visited):
        print("visited: "+str(visited))
        
        if node.value == value:
            return node

        elif not visited.has_key(node.value):
            
            visited[node.value] = True                    
            
            if self.compare(value, node.value) < 0 and node.left is not None:
                return self._depth_search(value, node.left, visited)
            
            elif self.compare(value, node.value) > 0  and node.right is not None:
                return self._depth_search(value, node.right, visited)                

            else: #value not found
                return None
            
    def breadth_search(self, value):
        if value is None:
            raise ValueError("Cannot search for null value")
        if self.root is not None:
            node_queue = Queue()
            node_queue.enqueue(self.root)
                        
            print("peek at node_queue: "+str(node_queue.peek().value))    
            
            while node_queue.is_empty() is False:
                check_node = node_queue.dequeue()
                print("check_node = "+str(check_node.value))
                print("node_queue.is_empty: "+str(node_queue.is_empty()))        
                
                if check_node.value == value:
                    return check_node
             
                elif self.compare(value, check_node.value) < 0 and check_node.left is not None:
                    node_queue.enqueue(check_node.left)
                elif self.compare(value, check_node.value) > 0 and check_node.right is not None:
                    node_queue.enqueue(check_node.right)
                else:
                    return None
                
                    
                
                
        
                
    def delete(self, value):
        if self.root.value == value and (self.root.left is not None or self.root.right is not None):
            raise ValueError("Mustn't delete root node when it has children!")        
        else:
            #self.root = 
            self._delete(value, self.root)
            

    def _delete(self, value, node):

        if node.value == value:
            parent_node = node.parent
            
            #need to know if the found node is the left or right of its parent
            parent_left_child = parent_node.left

            #parent_right_child = parent_node.right
        
            left_child = node.left #could be none
            right_child = node.right #could be none 
                        
            if left_child is not None and right_child is not None:
                # need to find leftmost node that is missing a left child
                # will return lft mst chldls node (could be right child itself)
                leftmost_childess_node = self._find_leftmost_childless_node(right_child)
                
                left_child.parent = leftmost_childess_node
                leftmost_childess_node.left = left_child

                if parent_left_child == node:
                    parent_node.left = right_child    
                else:
                    parent_node.right = right_child
                
                right_child.parent = parent_node    
                
            elif left_child is not None and right_child is None:
                left_child.parent = parent_node
                if parent_left_child == node:              
                    parent_node.left = left_child
                else:
                    parent_node.right = left_child
            
            elif left_child is None and right_child is not None:
                right_child.parent = parent_node
                if parent_left_child == node:              
                    parent_node.left = right_child
                else:
                    parent_node.right = right_child
            
            node = None
            
            #garbage collection will delete single node after all pointers are broken?
        
        else:
            if self.compare(value, node.value) < 0 and node.left is not None:
                self._delete(value, node.left)
            elif self.compare(value, node.value) > 0 and node.right is not None:
                self._delete(value, node.right)
            
         
        
    def _find_leftmost_childless_node(self, node): 
        if node.left is None:
            return node
        else:
            return self._find_leftmost_childless_node(node.left)
        
        
    
    def max_depth(self, node):        
        if not node.right and not node.left:
            return 0        
        right = left = 0
        if node.right:
            right = 1 + self.max_depth(node.right)
        if node.left:
            left = 1 + self.max_depth(node.left)
        return max(right, left)

    
    def print_tree(self):
        '''Print the tree rooted at root.'''
        self.print_helper(self.root, "")
    
    
    def print_helper(self, node, indent):
        '''Print the tree rooted at BTNode root. Print str indent (which
        consists only of whitespace) before the root value; indent more for the
        subtrees so that it looks nice.'''
        if node is not None:
            self.print_helper(node.right, indent + "   ")
            print indent + str(node.value)
            self.print_helper(node.left, indent + "   ")
