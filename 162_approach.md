# LeetCode 162 - Find Peak Element

## Problem

A peak element is an element that is strictly greater than its neighbors.

Given an integer array `nums`, find a peak element and return its index.

You may assume:

```text
nums[-1] = -∞
nums[n]  = -∞
```

The solution must run in:

```text
O(log n)
```

---

# Key Insight

This is not a searching problem.

This is a:

```text
Binary Search on Slope
```

problem.

Instead of asking:

```text
Where is the target?
```

we ask:

```text
Which direction is uphill?
```

---

# Visual Intuition

Consider:

```text
1 2 3 1
    ↑
   peak
```

At index 1:

```text
2 -> 3
```

We are moving uphill.

Therefore:

```text
Peak must exist on the right side.
```

---

Another example:

```text
1 2 5 3 1
    ↑
```

At index 2:

```text
5 -> 3
```

We are moving downhill.

Therefore:

```text
Peak is at mid or to the left.
```

---

# Core Observation

Compare:

```text
nums[mid]
nums[mid+1]
```

Only these two elements matter.

---

## Case 1

```text
nums[mid] > nums[mid+1]
```

Example:

```text
1 2 5 3 1
    M
```

We are on a descending slope.

A peak exists at `mid` or somewhere to the left.

Move:

```text
right = mid
```

---

## Case 2

```text
nums[mid] < nums[mid+1]
```

Example:

```text
1 2 3 5 7
      M
```

We are on an ascending slope.

A peak exists to the right.

Move:

```text
left = mid + 1
```

---

# Pseudocode

```text
left = 0
right = n-1

while left < right:

    mid = (left + right) // 2

    if nums[mid] > nums[mid+1]:
        right = mid

    else:
        left = mid + 1

return left
```

---

# Dry Run

Input:

```text
[1,2,3,1]
```

Initial:

```text
left = 0
right = 3
```

---

Iteration 1

```text
mid = 1

nums[mid] = 2
nums[mid+1] = 3

2 < 3
```

Move:

```text
left = mid + 1 = 2
```

---

Iteration 2

```text
left = 2
right = 3

mid = 2

nums[mid] = 3
nums[mid+1] = 1

3 > 1
```

Move:

```text
right = mid = 2
```

---

Now:

```text
left = right = 2
```

Answer:

```text
index = 2
```

---

# Why Binary Search Works

Every element belongs to one of two situations:

```text
Ascending slope
```

or

```text
Descending slope
```

A peak always lies in the direction where the slope eventually changes.

By repeatedly choosing the correct half, we eliminate half the search space each iteration.

---

# Complexity Analysis

## Time Complexity

```text
O(log n)
```

Binary search eliminates half the search space every iteration.

---

## Space Complexity

```text
O(1)
```

Only a few variables are used.

---

# Pattern Recognition

This problem belongs to:

```text
Binary Search on Structure
```

Similar problems:

* LC 33 - Search in Rotated Sorted Array
* LC 81 - Search in Rotated Sorted Array II
* LC 153 - Find Minimum in Rotated Sorted Array
* LC 540 - Single Element in a Sorted Array
* LC 162 - Find Peak Element

The common pattern is:

```text
Use binary search not on values,
but on a structural property of the array.
```

For LC 162 the property is:

```text
Slope Direction
```

Ask:

```text
nums[mid] > nums[mid+1] ?
```

If yes:

```text
Go Left
```

If no:

```text
Go Right
```

Eventually, the search converges to a peak.
