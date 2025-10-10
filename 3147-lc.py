class Solution:
    def maximumEnergy(self, energy: List[int], k: int) -> int:
        n = len(energy)
        ans = -10**18  # or float("-inf")
        for r in range(k):
         
            chain = []
            j = r
            while j < n:
                chain.append(energy[j])
                j += k
            
            suffix = 0
            best = -10**18
            for x in reversed(chain):
                suffix += x
                best = max(best, suffix)
            ans = max(ans, best)
        return ans
