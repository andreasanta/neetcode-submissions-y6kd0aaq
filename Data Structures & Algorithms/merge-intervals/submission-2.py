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

            print(f"current interval [{cur_start},{cur_end}]")
            print(f"new interval [{start},{end}]")

            # If the new interval is contained in the previous one, continue
            if cur_start <= start and end <= cur_end:
                print("new interval is contained, skipping")
                continue

            # Extend the current interval if overlaps, and ends further
            if start <= cur_end:
                print(f"extend {cur_end} => {end}")
                # Just squash the new end, we know the intervals are sorted
                current_interval = [cur_start, end]
            # No overlap, store current interval, and reopen a new one
            else:
                print(f"consolidate {cur_start} => {cur_end}")
                result.append(current_interval)

                print(f"new current {start} => {end}")
                current_interval = i

        result.append(current_interval)

        return result