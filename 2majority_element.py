# Majority element
# Due to the conversion from list -> set -> list, we are able to decrease the size of list and for loop time
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)>=1 and len(nums) <=50000:
            set_from_list = set(nums) # Converting list to set because a set will contain only unique values from the list
            unique_list = list(set_from_list) # Because of above conversion, we have a list of less size than given list/array
            majority_element = unique_list[0]
            for v in unique_list:
                if v < -pow(2,31) or v > pow(2,31)-1:
                    return
                if nums.count(v) > nums.count(majority_element):
                    majority_element = v

            if nums.count(majority_element) > len(nums)/2:
                return majority_element
        else:
            return

x = Solution()
nums = [1,1]#[2,2,1,1,1,2,2] #
print(x.majorityElement(nums))


'''
# Time Limit Exceeded
# Majority element
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        if len(nums)>=1 and len(nums) <=50000:
            majority_element = nums[0]
            for v in nums:
                if v < -pow(2,31) or v > pow(2,31)-1:
                    return
                if nums.count(v) > nums.count(majority_element):
                    majority_element = v

            if nums.count(majority_element) > len(nums)/2:
                return majority_element
        else:
            return
        
'''