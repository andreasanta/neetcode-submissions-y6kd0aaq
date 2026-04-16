class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        # Optimise away edge case, so we can iterate
        # starting from second element as well
        if len(intervals) == 1:
            return intervals

        
        # Take O(n * log(n)) hit to preprocess
        #
        # We have the guarantee that intervals will open
        # and close in order
        intervals.sort()

        current_interval = intervals[0]
        result = []

        for i in intervals[1:]:

            cur_start = current_interval[0]
            cur_end = current_interval[1]
            
            start = i[0]
            end = i[1]

            # Extend the current interval if overlaps, and ends further
            if start <= cur_end:
                # Just squash the new end, we know the intervals are sorted
                current_interval = [cur_start, max(end ,cur_end)]
            # No overlap, store current interval, and reopen a new one
            else:
                result.append(current_interval)
                current_interval = i

        result.append(current_interval)

        return result