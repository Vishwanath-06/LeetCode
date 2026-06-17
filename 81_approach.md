# Problem: LeetCode 81 - Search in Rotated Sorted Array II

## Approach:

- Use modified binary search.
- Determine whether left or right half is sorted.
- Check if the target lies within the sorted half.
- If duplicates make the sorted half ambiguous (nums[mid] == nums[right]), shrink the search space.
## Psuedo Code
```bash
L = 0
R = n-1

while L <= R:

    M = (L + R) // 2

    if nums[M] == target:
        return True

    ------------------------------------------------
    Case 1: Duplicates hide everything
    ------------------------------------------------

    if nums[L] == nums[M] == nums[R]:

        L += 1
        R -= 1

    ------------------------------------------------
    Case 2: Left half is sorted
    ------------------------------------------------

    elif nums[L] <= nums[M]:

        if nums[L] <= target < nums[M]:
            R = M - 1
        else:
            L = M + 1

    ------------------------------------------------
    Case 3: Right half is sorted
    ------------------------------------------------

    else:

        if nums[M] < target <= nums[R]:
            L = M + 1
        else:
            R = M - 1

return False
```
## Complexity:

Average: O(log n)
Worst Case (many duplicates): O(n)
Space: O(1)