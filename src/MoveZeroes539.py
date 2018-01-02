class Solution:
    """
    @param: nums: an integer array
    @return:
    """
    def switch(self,nums,i,j):
        temp = nums[i]
        nums[i] = nums[j]
        nums[j] = temp

    def moveZeroes(self, nums):
        # write your code here
        i=0
        j = len(nums)-1
        while i < j :
            if nums[i] == 0 and nums[j] != 0:
                    self.switch(nums,i,j)
                    i+=1
            j-=1

        return nums

solution = Solution()
print(solution.moveZeroes([0, 1, 0, 3, 12]))