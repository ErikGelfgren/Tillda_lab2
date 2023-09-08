class LinkedQ():
    def __init__(self):
        #Define first and last node in linked list
        self._first=None
        self._last=None

    def isEmpty(self):
        #Checks if First node is empty and returns True or False
        return self._first==None

    def enqueue(self,value):
        #Places new node in end of list and links it with last node
        new_val=Node(value)
        if self._first is None:
            self._first=new_val
            self._last=self._first
        else:
            self._last.next=new_val
            self._last=new_val

    def dequeue(self):
        #Stores value of first node and removes it from linked list
        value=self._first.value
        self._first=self._first.next
        return value

class Node():
    #Creates node with stored value and link to next node
    def __init__(self,value,next=None):
        self.value=value
        self.next=next
