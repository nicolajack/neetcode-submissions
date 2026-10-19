class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i = 0
        j = len(heights) - 1
        max_store = 0
        while i < j:
            cur_store = (j - i) * min(heights[i], heights[j])
            if cur_store > max_store:
                max_store = cur_store
            if heights[i] < heights[j]:
                i += 1
            else:
                j -= 1
        return max_store
