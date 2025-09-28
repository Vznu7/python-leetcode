import math

class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        triangle = []
        for n in range(numRows):
            row = [math.comb(n, k) for k in range(n + 1)]
            triangle.append(row)
        return triangle
