class LinkedQ():
    def __init__(self):
        self.first=None
        self.last=None

    def isEmpty(self):
        return self.first==None

    def enqueue(self,value):
        new_val=Node(value)
        if self.first is None:
            self.first=new_val
            self.last=self.first
        else:
            self.last.next=new_val
            self.last=new_val

    def dequeue(self):
        value=self.first.value
        self.first=self.first.next
        return value

class Node():
    def __init__(self,value,next=None):
        self.value=value
        self.next=next
    
