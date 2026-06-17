# LeetCode 540 - Single Element in a Sorted Array

## Problem

Given a sorted array where every element appears exactly twice except for one element which appears only once, find the single element.

Example:

```text
[1,1,2,3,3,4,4]
```

Output:

```text
2
```

---

# Approach 1: Linear Scan

## Intuition

Since the array is sorted:

```text
1 1 | 2 2 | 3 3 | 4
```

Every valid pair occupies adjacent positions.

Walk through the array in steps of 2:

* If a pair matches, continue.
* If a pair breaks, the first element is the answer.
* If all pairs match, the last element is the answer.

## Pseudocode

```text
i = 0

while i < n-1:

    if nums[i] != nums[i+1]:
        return nums[i]

    i += 2

return nums[n-1]
```

## Complexity

Time: O(n)

Space: O(1)

---

# Approach 2: Binary Search (Optimal)

## Key Observation

Before the single element:

```text
Index: 0 1 2 3 4 5
Value: 1 1 2 2 3 3
```

Pairs start at even indices.

```text
0, 2, 4, ...
```

After the single element:

```text
Index: 0 1 2 3 4 5 6
Value: 1 1 2 3 3 4 4
```

Pairs start at odd indices.

```text
3, 5, ...
```

The single element causes a shift in the pairing pattern.

---

## Binary Search Idea

Choose a middle index.

Make sure it is even.

Compare:

```text
nums[mid]
nums[mid+1]
```

### Case 1

```text
nums[mid] == nums[mid+1]
```

The pairing pattern is still correct.

The single element must be on the right.

Move:

```text
left = mid + 2
```

---

### Case 2

```text
nums[mid] != nums[mid+1]
```

The pairing pattern breaks here.

The single element is at mid or to the left.

Move:

```text
right = mid
```

---

## Pseudocode

```text
left = 0
right = n-1

while left < right:

    mid = (left + right) // 2

    if mid is odd:
        mid -= 1

    if nums[mid] == nums[mid+1]:
        left = mid + 2
    else:
        right = mid

return nums[left]
```

---

## Example

Input:

```text
[1,1,2,3,3,4,4]
```

Iteration 1:

```text
mid = 2

nums[2] = 2
nums[3] = 3

Mismatch
```

Move:

```text
right = mid
```

Continue shrinking until:

```text
left == right
```

Answer:

```text
2
```

---

## Complexity

### Binary Search

Time: O(log n)

Space: O(1)

### Linear Scan

Time: O(n)

Space: O(1)

---

## Pattern Recognition

This problem belongs to the Binary Search on Structure category.

Instead of searching for a value:

```text
Is the pairing pattern still valid?
```

If yes:

```text
Go right.
```

If no:

```text
Go left.
```

The answer is exactly where the pairing pattern breaks.

