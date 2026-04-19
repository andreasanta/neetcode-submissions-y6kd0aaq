from typing import List

class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        
        cur_word_idx = 0
        ret_val = []

        while cur_word_idx < len(words):

            cur_row = []
            cur_len = 0

            # Append words until we exceed or match max width
            while cur_word_idx < len(words):
                
                cur_word = words[cur_word_idx]
                cur_word_len = len(cur_word)

                # Account for ONE space if not the first word
                space = 1 if len(cur_row) != 0 else 0

                # Word overruns or fills row, break without adding it
                if cur_len + cur_word_len + space > maxWidth:
                    break

                cur_row.append(cur_word)
                cur_word_idx += 1                
                cur_len += space + cur_word_len

            # Edge case when we match max width exactly,
            # means either spaces are equally distributed
            # or there is one single word, just print the line
            # without special adjustments
            if cur_len == maxWidth:
                #print("Print entire line w/o adjustments " + str(cur_row))
                ret_val.append(self.print_line(cur_row))
                cur_row = []
                cur_len = 0
                continue

            # Here we have leftover spaces to the right,
            # we can use the same algo to pad between
            # words even with one word
            leftover_spaces = maxWidth - cur_len

            # Edge case for last row
            if cur_word_idx == len(words):
                # Left justify as per requirements
                ret_val.append(" ".join(cur_row) + (" " * leftover_spaces))
                break

            # Gaps in between words are equal to the number of spaces, i.e. words - 1
            gaps = len(cur_row) - 1
            
            # Base case, no extra dividing spaces
            #
            # If there are no gaps, we have no dividing spaces
            # and all the leftover spaces are at the end
            dividing_spaces = 0
            remaning_spaces = leftover_spaces
            
            # If there are gaps, calculate how many spaces we should add
            # per each gap, and how many extra spaces (reminder) we need
            # to distribute across the row
            if gaps > 0:
                dividing_spaces = leftover_spaces // gaps
                remaning_spaces = leftover_spaces % gaps


            #print("Calculations for line " + str(cur_row))
            #print(f"leftover = {leftover_spaces}, dividing = {dividing_spaces}, remaning = {remaning_spaces}")

            # All spaces are evenly distributed, print with equal padding
            # Means we have exactly n * gaps spaces.
            if remaning_spaces == 0:
                ret_val.append(self.print_line(cur_row, dividing_spaces))

            else:
            # This is the most complex case, we have spaces distributed
            # equally, and extra spaces distributed from left to right
                ret_val.append(self.print_line(cur_row, dividing_spaces, remaning_spaces))


        return ret_val        

    def print_line(self, row, extra_spaces_per_word = 0, extra_spaces_distribution = 0):

        text = ""

        for i,s in enumerate(row):
            if i != 0:
                
                text += " "
                text += " " * extra_spaces_per_word

                if extra_spaces_distribution > 0:
                    text += " "
                    extra_spaces_distribution -= 1
            
            text += s

        # Append spaces after last word, if left
        text += " " * extra_spaces_distribution

        return text



