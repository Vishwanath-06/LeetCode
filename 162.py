```python
from typing import List


class Solution:
    """
    Binary Search Solution
    Time Complexity: O(log n)
    Space Complexity: O(1)
    """

    def findPeakElement(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1

        while left < right:
            mid = (left + right) // 2

            if nums[mid] > nums[mid + 1]:
                right = mid
            else:
                left = mid + 1

        return left


def run_tests():
    solution = Solution()

    test_cases = [
        ([1], 0),
        ([1, 2, 3, 1], 2),
        ([1, 2, 1, 3, 5, 6, 4], 5),
        ([1, 2], 1),
        ([2, 1], 0),
        ([1, 2, 3, 4, 5], 4),
        ([5, 4, 3, 2, 1], 0),
    ]

    for i, (nums, expected) in enumerate(test_cases, start=1):
        result = solution.findPeakElement(nums)

        print(
            f"Test {i}: "
            f"{'PASS' if result == expected else 'CHECK'} | "
            f"Expected={expected}, Got={result}"
        )


if __name__ == "__main__":
    run_tests()