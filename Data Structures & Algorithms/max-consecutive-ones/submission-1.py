class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_streak = 0
        current_streak = 0
        
        for num in nums:
            if num == 1:
                current_streak += 1
                # Update max_streak if the current streak is higher
                max_streak = max(max_streak, current_streak)
            else:
                # Streak broken, reset current counter
                current_streak = 0
                
        return max_streak

        