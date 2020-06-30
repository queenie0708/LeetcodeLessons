from itertools import combinations
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        n = len(nums)
        if n == 3:
            return sum(nums)
        coms = list(combinations(nums, 3))
        mins = [sum(coms[0])-target]
        if mins[0] == 0:
            return target
        for i in coms:
            if abs(sum(i) - target) < abs(mins[0]):
                mins.pop()
                mins.append(sum(i) - target)
                if mins[0] == 0:
                    return target
        return mins[0] + target