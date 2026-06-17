from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return True

            # Right half is sorted
            if nums[mid] < nums[right]:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1

            # Left half is sorted
            elif nums[mid] > nums[right]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1

            # Duplicates obscure which half is sorted
            else:
                right -= 1

        return False


def run_tests():
    solution = Solution()

    test_cases = [
        # LeetCode examples
        ([2, 5, 6, 0, 0, 1, 2], 0, True),
        ([2, 5, 6, 0, 0, 1, 2], 3, False),

        # Not rotated
        ([1, 2, 3, 4, 5], 3, True),
        ([1, 2, 3, 4, 5], 6, False),

        # Single element
        ([1], 1, True),
        ([1], 0, False),

        # All duplicates
        ([1, 1, 1, 1, 1], 1, True),
        ([1, 1, 1, 1, 1], 2, False),

        # Duplicates with rotation
        ([1, 0, 1, 1, 1], 0, True),
        ([1, 1, 1, 1, 0, 1], 0, True),

        # Target at boundaries
        ([4, 5, 6, 7, 0, 1, 2], 4, True),
        ([4, 5, 6, 7, 0, 1, 2], 2, True),

        # Edge cases
        ([3, 1], 1, True),
        ([3, 1], 0, False),
    ]

    passed = 0

    for i, (nums, target, expected) in enumerate(test_cases, start=1):
        result = solution.search(nums, target)

        if result == expected:
            print(f"✅ Test {i} PASSED")
            passed += 1
        else:
            print(
                f"❌ Test {i} FAILED\n"
                f"   nums={nums}\n"
                f"   target={target}\n"
                f"   expected={expected}\n"
                f"   got={result}\n"
            )

    print(f"\nPassed {passed}/{len(test_cases)} tests")


if __name__ == "__main__":
    run_tests()