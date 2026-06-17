# LeetCode 153 - Find Minimum in Rotated Sorted Array

## Problem

Given a sorted array that has been rotated between 1 and n times, find the minimum element.

Example:

```text
[4,5,6,7,0,1,2]
```

Output:

```text
0
```

---

## Key Observation

A rotated sorted array consists of two regions:

```text
BIG VALUES | SMALL VALUES
```

Example:

```text
[4,5,6,7 | 0,1,2]
```

The minimum element is the first element in the smaller region.

---

## Binary Search Intuition

Instead of searching for a target, we search for the boundary between the two regions.

Compare:

```text
nums[mid]
```

with

```text
nums[right]
```

---

### Case 1

```text
nums[mid] > nums[right]
```

Example:

```text
[4,5,6,7,0,1,2]
       M     R

7 > 2
```

This means `mid` belongs to the larger region.

The minimum must be to the right of `mid`.

Move:

```text
left = mid + 1
```

---

### Case 2

```text
nums[mid] < nums[right]
```

Example:

```text
[4,5,6,0,1,2]
     M     R

0 < 2
```

This means `mid` belongs to the smaller region.

The minimum could be at `mid` itself.

Move:

```text
right = mid
```

Notice we keep `mid` because it may be the answer.

---

## Pseudocode

```text
left = 0
right = n - 1

while left < right:

    mid = (left + right) // 2

    if nums[mid] > nums[right]:
        left = mid + 1
    else:
        right = mid

return nums[left]
```

---

## Example Walkthrough

Input:

```text
[4,5,6,7,0,1,2]
```

Iteration 1:

```text
left = 0
right = 6
mid = 3

nums[mid] = 7
nums[right] = 2

7 > 2
```

Move:

```text
left = mid + 1 = 4
```

---

Iteration 2:

```text
left = 4
right = 6
mid = 5

nums[mid] = 1
nums[right] = 2

1 < 2
```

Move:

```text
right = mid = 5
```

---

Iteration 3:

```text
left = 4
right = 5
mid = 4

nums[mid] = 0
nums[right] = 1

0 < 1
```

Move:

```text
right = 4
```

Now:

```text
left = right = 4
```

Answer:

```text
nums[4] = 0
```

---

## Complexity Analysis

### Time Complexity

```text
O(log n)
```

At every step, half of the search space is discarded.

### Space Complexity

```text
O(1)
```

Only a few variables are used.

---

## Pattern Recognition

This problem belongs to the Rotated Sorted Array family:

* LeetCode 33 — Search in Rotated Sorted Array
* LeetCode 81 — Search in Rotated Sorted Array II
* LeetCode 153 — Find Minimum in Rotated Sorted Array
* LeetCode 154 — Find Minimum in Rotated Sorted Array II

The common idea is:

```text
Use nums[mid] and nums[right]
to determine which side contains the answer.
```
