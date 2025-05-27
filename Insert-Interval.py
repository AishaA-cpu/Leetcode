class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        intervals.sort(key=lambda x:x[0])
        res = [intervals[0]]
        for i in range(1, len(intervals)):
            start, stop = intervals[i]
            if start <= res[-1][-1]:
                res[-1][-1] = max(stop, res[-1][-1])
            else:
                res.append([start, stop])

        return res

