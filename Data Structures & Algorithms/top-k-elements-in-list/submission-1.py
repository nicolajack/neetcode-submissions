class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ht = {}
        for num in nums:
            if num in ht:
                ht[num] += 1
            else:
                ht[num] = 1
        pq = []
        for key in ht.keys():
            heapq.heappush(pq, ((-1 * ht[key]), key))
        sol = []
        for i in range(k):
            tup = heapq.heappop(pq)
            sol.append(tup[1])
        return sol
