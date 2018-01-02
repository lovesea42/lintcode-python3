class Solution:
    """
    @param: n: an integer
    @return: an ineger f(n)
    """
    def fibonacci(self, n):
        # write your code here
        first,second = 0,1
        ret = 1
        if n == 1:
            return 0
        if n == 2:
            return 1
        index = 0
        while index <= n-3:
            ret = first + second
            first = second
            second = ret
            index += 1

        return ret


