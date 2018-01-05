class Solution:
    """
    @param: A: an integer array
    @return:
    """
    def sortIntegers(self, A):
        # write your code here
        B = []
        for tmp in A :
            if len(B) == 0:
                B.append(tmp)
            else:
                lenB = len(B)
                for i in range(0,lenB):
                    if tmp > B[i]:
                        continue
                    else:
                        B.insert(i,tmp)
                        break
                len2B = len(B)
                if len2B == lenB:
                    B.append(tmp)

        A.clear()
        for tmp in B:
            A.append(tmp)


sl = Solution()
A= [3, 2, 1, 4, 5]
sl.sortIntegers(A)
print(A)