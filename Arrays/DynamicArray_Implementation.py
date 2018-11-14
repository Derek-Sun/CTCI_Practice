'''Implementation of Dynamic Array in Python Following Udemy Course'''


import ctypes

class DynamicArray(object):

    def __init__(self):
        #Keep track of length of array
        self.length = 0
        #Keep track of max capacity of array
        self.capacity = 1
        #Make Array with specidied capacity
        self.Array = self.make_array(self.capacity)

    #Return length of the array when 
    def __len__(self):
        return self.length
    
    def __getitem__(self, index):
        if not 0 <= index < self.length:
            return IndexError('Index is out of bounds!')
        
        return self.Array[index]

    def append(self, element):
        #Double the capacity when max capacity is reached
        if self.length == self.capacity:
            self._resize(2 * self.capacity)
        
        self.Array[self.length] = element
        self.length += 1
    
    def _resize(self, newCapacity):

        newArray = self.make_array(newCapacity)

        for k in range(self.length):
            newArray[k] = self.Array[k]
        
        self.Array = newArray
        self.capacity = newCapacity

    def make_array(self, newCapacity):
        return (newCapacity * ctypes.py_object)()
    

Arr = DynamicArray()
Arr.append(1)
print(len(Arr))
Arr.append(2)
print(len(Arr))
print(Arr[0])
print(Arr[1])