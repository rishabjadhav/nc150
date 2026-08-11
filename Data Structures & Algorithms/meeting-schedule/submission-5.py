"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        '''
        sort by start time, then compare adjacent intervals for overlap, if detected, res = false
        '''

        res = True
        intervals.sort(key=lambda x: x.start)

        i = 0
        while i + 1 < len(intervals):
            if intervals[i+1].start < intervals[i].end:
                res = False
            i += 1
        
        return res
