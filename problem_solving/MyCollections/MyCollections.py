#!/usr/bin/env python
# coding: utf-8

# In[35]:


class Stack:
    
    def __init__(self):
        self.lst=[]
        
    def push(self,element):
        self.lst.append(element)
        print('pushed :',element)
        
    def pop(self):
        if self.size() > 0:
            s= self.lst.pop()
            print('popped : ',s)
            return s
        else:
            return None
        
    def size(self):
        return len(self.lst)
    
    def peak(self):
        if (len(self.lst) >0):
            return self.lst[0]
    
    def __str__(self):
        returnstr='stack : '
        for x in self.lst:
            returnstr += str(x)+' '
        return returnstr


# In[33]:


class Queue:
    
    def __init__(self):
        print('Queue initialized')
        self.lst = []
        
    def enqueue(self,element):
        self.lst.append(element)
        print('Enqueued : ',element)
        
    def dequeue(self):
        if self.size() > 0:
            element = self.lst.pop(0)
            print('Dequeued : ',element)
            return element
        else:
            return None
        
    def size(self):
        return len(self.lst)
    
    def peak(self):
        if (len(self.lst) >0):
            return self.lst[0]
    
    def __str__(self):
        returnstring = 'Queue : '
        for x in self.lst:
            returnstring += str(x)+' '
        return returnstring


# In[36]:


from collections import defaultdict
class Graph:
    
    def __init__(self):
        print('Graph instatiated')
        self.graph = defaultdict(list)
        
    def addVertex(self,parent,child=None):
        if child:
            self.graph[parent].append(child)
        else:
            self.graph[parent].append([])
        
    def __str__(self):
        returnstr = ''
        for k,v in self.graph.items():
            returnstr += str(k)+'-->'+''.join([str(x) for x in v]) + '\r\n'
        return returnstr
    def getparent(self,root):
        for k,v in self.graph.items():
            if root in v:
                return k


# In[ ]:




