from Interfaces import Stack
import SLLStack


class MaxStack(Stack) :
    def __init__(self):
        self.stack = SLLStack.SLLStack()
        
    def max(self) ->object: #Modify
        '''
            Returns the max element
        '''
        current = self.stack.head
        max = self.stack.head.x
        while (current != None):
            if (max < current.x):
                max = current.x
            current = current.next
        return max

    
    def push(self, x : object) : #Modify
        '''
            push: Insert an element in the tail of the stack 
            Inputs:
                x: Object type, i.e., any object
        '''
        return self.stack.push(x)



    def pop(self) -> object: #Modify
        '''
            pop: Remove the last element in the stack 
            Returns: the object of the tail if it is no empty
        '''
        return self.stack.pop()


    def size(self) -> int:
        return self.stack.size()

'''m = MaxStack()
#m.pop()
m.push(3)
m.push(1)
m.push(4)
m.push(2)

print(m.stack)

print("max:",m.max()) #4

print("remove:",m.pop()) #2
print("remove:",m.pop()) #4

print(m.stack)

print("max:",m.max()) #3

print("remove:",m.pop()) #1

print(m.stack)

print("max:",m.max()) #3'''
