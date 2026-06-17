from typing import List


class Solution:
    """
    Optimal Binary Search Solution
    Time Complexity: O(log n)
    Space Complexity: O(1)
    """

    def singleNonDuplicate(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1

        while left < right:
            mid = (left + right) // 2

            # Ensure mid is even
            if mid % 2 == 1:
                mid -= 1

            if nums[mid] == nums[mid + 1]:
                left = mid + 2
            else:
                right = mid

        return nums[left]


class LinearSolution:
    """
    Linear Scan Solution
    Time Complexity: O(n)
    Space Complexity: O(1)
    """

    def singleNonDuplicate(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        i = 0

        while i < len(nums) - 1:
            if nums[i] != nums[i + 1]:
                return nums[i]

            i += 2

        return nums[-1]


def run_tests():
    binary = Solution()
    linear = LinearSolution()

    test_cases = [
        ([1], 1),
        ([1, 1, 2], 2),
        ([1, 2, 2], 1),
        ([1, 1, 2, 3, 3], 2),
        ([1, 1, 2, 2, 3], 3),
        ([1, 1, 2, 3, 3, 4, 4], 2),
        ([3, 3, 7, 7, 10, 11, 11], 10),
        ([1, 1, 2, 2, 4, 4, 5, 5, 9], 9),
    ]

    print("Testing Binary Search Solution")
    for nums, expected in test_cases:
        result = binary.singleNonDuplicate(nums)
        print(
            f"{'PASS' if result == expected else 'FAIL'} | "
            f"Expected={expected}, Got={result}"
        )

    print("\nTesting Linear Solution")
    for nums, expected in test_cases:
        result = linear.singleNonDuplicate(nums)
        print(
            f"{'PASS' if result == expected else 'FAIL'} | "
            f"Expected={expected}, Got={result}"
        )


if __name__ == "__main__":
    run_tests()

