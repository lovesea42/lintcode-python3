class Solution:

    def getLetter(self, digit):
        if digit == 2:
            return 'abc'
        elif digit == 3:
            return 'def'
        elif digit == 4:
            return 'ghi'
        elif digit == 5:
            return 'jkl'
        elif digit == 6:
            return 'mno'
        elif digit == 7:
            return 'pqrs'
        elif digit == 8:
            return 'tuv'
        elif digit == 9:
            return 'wxyz'
    """
    @param: digits: A digital string
    @return: all posible letter combinations
    """
    def letterCombinations(self, digits):
        # write your code here
