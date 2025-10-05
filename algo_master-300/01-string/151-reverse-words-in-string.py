class Solution:
    def reverseWords(self, s: str) -> str:
        
        return " ".join(s.split()[::-1])

#another approach
class Solution:
    def reverseWords(self, s: str) -> str:
        lst = s.split()
        lst.reverse()
        return " ".join(lst)


        