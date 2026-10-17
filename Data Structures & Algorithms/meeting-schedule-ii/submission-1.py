"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        start = sorted([i.start for i in intervals])
        end = sorted([i.end for i in intervals])
        st = en = maxx = count = 0
        while st < len(start) and en < len(end):
            if start[st] < end[en]:
                st += 1
                count += 1
                maxx = max(maxx, count)
            else:
                count -= 1
                en += 1
        return maxx