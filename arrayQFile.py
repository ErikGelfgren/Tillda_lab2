import array



class ArrayQ:



    def __init__(self):

        self.array=array.array('i')



    def enqueue(self,element):

        self.array.append(element)

        return self.array

    

    def dequeue(self):

        value=self.array.pop(0)

        return value

    

    def size(self):

        n=len(self.array)

        return n

    def isEmpty(self):

        if len(self.array)==0:

            return True

        else:

            return False

