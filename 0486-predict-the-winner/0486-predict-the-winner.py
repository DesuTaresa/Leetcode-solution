from functools import lru_cache
from typing import List


class Solution:

  def predictTheWinner(self, nums: List[int]) -> bool:
    @lru_cache(None)
    def max_diff(i: int, j: int) -> int:
      
      if i == j:
        return nums[i]

      pick_left = nums[i] - max_diff(i + 1, j)
      pick_right = nums[j] - max_diff(i, j - 1)

      return max(pick_left, pick_right)

    return max_diff(0, len(nums) - 1) >= 0