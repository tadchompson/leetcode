"""
Given a non-empty array of integers, return the k most frequent elements.

For example,
Given [1,1,1,2,2,3] and k = 2, return [1,2].

Note: 
You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
"""
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        freq = []
        h_map = {}
        answer = []
        for num in nums:
            if num not in h_map:
                h_map[num] = 1
            else:
                h_map[num]+=1
        for key in h_map.keys():
            freq.append((-h_map[key], key))
        heapq.heapify(freq)
        for i in range(k):
            answer.append(heapq.heappop(freq)[1])
        return answer
