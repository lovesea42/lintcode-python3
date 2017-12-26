class MinStack:
    def __init__(self):

     self.lst,self.minl=[],[]
    # do intialization if necessary

    """
    @param: number: An integer
    @return: nothing
    """

    def push(self, number):
       self.lst.append(number)
       if(len(self.minl) == 0 or self.minl[-1] >= number):
           self.minl.append(number)



    # write your code here

    """
    @return: An integer
    """

    def pop(self):

        ret = self.lst[-1]
        del self.lst[-1]
        if self.minl[-1] == ret:
            del(self.minl[-1])
        return ret
    # write your code here

    """
    @return: An integer
    """

    def min(self):
        return self.minl[-1]
# write your code here

stack = MinStack()
stack.push(1)
print(stack.pop())
stack.push(2)
stack.push(3)
print(stack.min())
stack.push(1)
print(stack.min())