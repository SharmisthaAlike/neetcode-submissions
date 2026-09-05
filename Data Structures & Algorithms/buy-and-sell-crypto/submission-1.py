class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minp=prices[0]
        max_p=0
        for p in prices:
            minp=min(minp,p)
            prof=p-minp
            max_p=max(max_p,prof)

        return max_p