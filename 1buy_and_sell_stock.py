# Best time to buy and sell stock - 1
# Time complexity = O(n), run time 16ms
class Solution(object):
    def maxProfit(self, prices):
        '''
        type prices: List[int]
        rtype: int
        '''
        if min(prices) >= 0 and max(prices) <= 10000:
            min_price = 10001 #initially set a very high value so that when it's compared with first price, min_price will become that price because that will be lower only, than this value.
            max_profit = 0
            for i in range(len(prices)):
                min_price = min(min_price, prices[i])
                max_profit = max(max_profit, prices[i] - min_price)
            if max_profit > 0:
                return max_profit
            else:
                return 0

prices = [2,1,4] #[7,6,4,3,1] #[2,4,1] #[7,1,5,3,6,4], [2,1,4],
output = Solution().maxProfit(prices)
print(output)

"""
# This solution give right answer but takes more time than allowed and gives error : "Time Limit Exceeded" on LeetCode
# Time Complexity = O(n^2), runtime 46ms
class Solution(object):
    def maxProfit(self, prices):
        '''
        type prices: List[int]
        rtype: int
        '''
        if min(prices) >= 0 and max(prices) <= 10000:
            max_profit = 0
            for i in range(len(prices)-1):
                for j in range(i,len(prices)):
                    if (prices[j] - prices[i]) > max_profit:
                        max_profit = prices[j] - prices[i]

            if max_profit > 0:
                return max_profit
            else:
                return 0
"""

"""
# Wrong method because it's not comparing pairs. Ex. it won't give correct answer for [2,4,1]
class Solution(object):
    def maxProfit(self, prices):
        '''
        type prices: List[int]
        rtype: int
        '''
        if min(prices) >= 0 and max(prices) <= 10000:
            lowest = min(prices)
            lowest_index = prices.index(lowest)
            
            next_highest = max(prices[lowest_index:])
            next_highest_index = prices.index(next_highest)
            print(next_highest_index - lowest_index)
            if (next_highest_index - lowest_index) > 0:
                max_profit = next_highest - lowest
                print(prices,next_highest,next_highest_index,lowest,lowest_index,max_profit)
                return max_profit
            else:
                return 0

"""