class Solution:
    """
    @param k:
    @return: the sum of first k even-length palindrome numbers
    """
    def sumKEven(self, k):
        # Write your code here
        ret = 0
        for i in range(k):
            ret += self.getPalindrome(i+1)

        return ret

    def getPalindrome(self,i):
        left = str(i)
        right = left[::-1]
        return int(left + right)


solution = Solution()
print (solution.sumKEven(10))