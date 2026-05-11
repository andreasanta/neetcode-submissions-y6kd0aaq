class Solution:

    ESCAPED = '^|'
    ESCAPE = '^'
    DELIM = '|'

    def encode(self, strs: List[str]) -> str:

        if not strs:
            return chr(0)

        words = []

        for word in strs:

            word = word.replace(self.DELIM, self.ESCAPED)
            words.append(word)


        out = self.DELIM.join(words)
        #print("Encoded", out)

        return out



    def decode(self, s: str) -> List[str]:

        if s == chr(0):
            return []

        words = []
        word = ''
        i = 0

        while i < len(s):

            cur_char = s[i]

            #print("Index", i)
            #print("Cur char", cur_char)

            if cur_char == self.ESCAPE:

                #print("Escape detected")

                if i < len(s)-1 and s[i+1] == self.DELIM:

                    #print("Followed by delimiter")

                    word += self.DELIM
                    i += 2

                    continue

            if cur_char == self.DELIM:
                #print("Delimiter found, split")
                words.append(word)
                word = ''
                i += 1
                continue

            i += 1
            word += cur_char

        words.append(word)

        return words
