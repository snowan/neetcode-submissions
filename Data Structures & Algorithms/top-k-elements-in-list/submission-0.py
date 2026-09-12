class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for num in nums:
            freq[num] = 1 + freq.get(num, 0)
        
        min_heap = []
        for key, val in freq.items():
            if len(min_heap) < k:
                heapq.heappush(min_heap, (val, key))
            else:
                top_val, top_key = min_heap[0]
                if top_val < val:
                    heapq.heappop(min_heap)
                    heapq.heappush(min_heap, (val, key))
        
        return [key for val, key in min_heap]
