class Solution:
    """
    @param: A: an integer rotated sorted array
    @param: target: an integer to be searched
    @return: an integer
    """
    def search2(self, A, target):
        length = len(A)
        # write your code here
        for i in range(length):
            if A[i] == target:
                return i
        return -1


solution = Solution()
print(solution.search([4,5,1,2,3],1))