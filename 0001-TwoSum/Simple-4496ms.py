class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        numlst = list(range(len(nums)))
        for numidx in numlst:
            othernum = target - nums[numidx]
            otherlst = nums[numidx + 1:]

            for otheridx in list(range(len(otherlst))):
                if othernum == otherlst[otheridx]:
                    return [numidx, numidx + otheridx + 1]

'''
num_list = [3, 2, 4]
target_num = 6
print(Solution().twoSum(num_list, target_num))
'''
