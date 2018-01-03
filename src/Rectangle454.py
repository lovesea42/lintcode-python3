class Rectangle:
    '''
     * Define a constructor which expects two parameters width and height here.
    '''
    width,height = 0,0
    # write your code here

    def __init__(self,width,height):
        self.height = height
        self.width = width

    '''
     * Define a public method `getArea` which can calculate the area of the
     * rectangle and return.
    '''
    # write your code here
    def getArea(self):
        return self.width * self.height