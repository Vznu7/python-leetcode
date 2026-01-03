class Solution(object):
    def romanToInt(self, s):
      #this is a big o(n) method
        roman = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        t = 0
        prev = 0

        for ch in reversed(s): 
            curr = roman[ch]
            if curr < prev:
                t -= curr
            else:
                t += curr
            prev = curr

        return t
