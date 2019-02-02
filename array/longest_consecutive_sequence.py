Given an unsorted array of integers, find the length of the longest consecutive elements sequence.

Your algorithm should run in O(n) complexity.

Example:

Input: [100, 4, 200, 1, 3, 2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.



class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        longest = 0 
        num_set = set(nums)
        
        for num in num_set:
          if num - 1 not in num_set:
            current_length = 1

            while num + 1 in num_set:
              num += 1 
              current_length += 1

            longest = max(longest, current_length)
          
        return longest 