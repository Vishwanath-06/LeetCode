from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1

        while left < right:
            mid = (left + right) // 2

            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid

        return nums[left]


def run_tests():
    solution = Solution()

    test_cases = [
        ([3, 4, 5, 1, 2], 1),
        ([4, 5, 6, 7, 0, 1, 2], 0),
        ([11, 13, 15, 17], 11),
        ([2, 1], 1),
        ([1], 1),
        ([5, 1, 2, 3, 4], 1),
        ([2, 3, 4, 5, 1], 1),
    ]

    passed = 0

    for i, (nums, expected) in enumerate(test_cases, start=1):
        result = solution.findMin(nums)

        if result == expected:
            print(f"✅ Test {i} PASSED")
            passed += 1
        else:
            print(
                f"❌ Test {i} FAILED\n"
                f"   nums={nums}\n"
                f"   expected={expected}\n"
                f"   got={result}\n"
            )

    print(f"\nPassed {passed}/{len(test_cases)} tests")


if __name__ == "__main__":
    run_tests()