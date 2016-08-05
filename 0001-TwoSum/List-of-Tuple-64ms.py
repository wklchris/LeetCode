class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        ziplst = list(zip(nums, list(range(len(nums)))))
        ziplst.sort()
        # ziplst is like this: [(2, 1), (3, 0), (4, 2)]

        idx_1, idx_2 = 0, len(nums) - 1
        while idx_1 < idx_2:
            sumnum = ziplst[idx_1][0] + ziplst[idx_2][0]
            if sumnum < target:
                idx_1 += 1
            elif sumnum > target:
                idx_2 -= 1
            else:
                return [ziplst[idx_1][1], ziplst[idx_2][1]]
        # Else
        return 'No match'


# For Test

'''
num_list = [3, 2, 4]
target_num = 7
print(Solution().twoSum(num_list, target_num))
'''
