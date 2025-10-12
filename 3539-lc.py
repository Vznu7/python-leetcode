import functools, math

class Solution:
    MOD = 10**9 + 7

    def magicalSum(self, m: int, k: int, nums: list[int]) -> int:
        @functools.lru_cache(None)
        def dp(rem_m: int, rem_k: int, i: int, carry: int) -> int:
            # invalid states
            if rem_m < 0 or rem_k < 0 or (rem_m + carry.bit_count() < rem_k):
                return 0
            if rem_m == 0:
                return 1 if rem_k == carry.bit_count() else 0
            if i == len(nums):
                return 0

            res = 0
            # try taking count copies of nums[i] (0..rem_m)
            for count in range(rem_m + 1):
                comb = math.comb(rem_m, count)  # C(rem_m, count)
                contribution = comb * pow(nums[i], count, self.MOD) % self.MOD
                new_carry = carry + count
                # next rem_k decreases by parity of new_carry (lowest bit)
                res += dp(rem_m - count, rem_k - (new_carry & 1), i + 1, new_carry >> 1) * contribution
                res %= self.MOD
            return res

        return dp(m, k, 0, 0)
