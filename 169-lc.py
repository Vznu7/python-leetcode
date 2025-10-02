

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        result,count =0,0
        for n in nums:
            if count==0:
                result =n
            count+=( 1 if result == n else -1)
        return result


### another so
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counter ={}
        for n in nums:
            if n in counter:
                counter[n]+=1
            else:
                counter[n] =1
        
        result,max =-1,-1
        for n,c in counter.items():
            if c>max:
                result,max =n,c
        return result

    
        