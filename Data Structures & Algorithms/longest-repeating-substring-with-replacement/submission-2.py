class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        if len(s) < 2:
            return len(s)
        
        freq_map = {}
        l, r = 0, 1
        max_len = 1

        # Add the first char
        freq_map = {
            s[l]: 1
        }

        while r < len(s):

            rchar = s[r]
            window_len = r - l + 1

            #print("Window l", l, "r", r, "len", window_len)
            #print("New char", rchar)

            if not rchar in freq_map:
                freq_map[rchar] = 0

            freq_map[rchar] += 1            
            max_freq = 0

            for c,f in freq_map.items():
                #print("Freq", f, "for", c)
                max_freq = max(max_freq, f)

            if window_len - max_freq > k:
                freq_map[s[l]] -= 1
                l += 1
            else:
                max_len = max(max_len, window_len)

            r += 1

        return max_len


            



