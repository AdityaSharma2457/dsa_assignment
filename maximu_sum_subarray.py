class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        arr=nums
        max_sum=arr[0]
        curr_sum=0
        for i in range(len(nums)):
            curr_sum=max(curr_sum+arr[i],arr[i])
            max_sum=max(max_sum,curr_sum)
        return max_sum
