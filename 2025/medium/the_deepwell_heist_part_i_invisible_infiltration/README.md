---
challenge: The Deepwell Heist Part I: Invisible Infiltration
description: "The Deepwell Archive. The most secure data storage system in the entire galaxy, housing a full backup of thousands of years of data from across the Milky Way. Surely, whatever information is kept inside would be more valuable than any wealth imaginable. Your crew has their eyes set on that data. It won't be easy, of course: the Archive's security is the best in the galaxy, and only the most concise code can be injected without instant lockout. Good luck.\n\n*The team with the shortest code will receive bonus points.*\n\n*This activity is in-person, in the Deepwell Archive.*"
flag: ATR{sl33k_c0d1ng}
scoring: subflags(250, 250)
value: 500
category: Medium
authors: Alice Arvidson
---

# The Deepwell Heist Part I: Invisible Infiltration

[Back to Home](../../README.md)

## Points

Medium - 500 points

## Description

The Deepwell Archive. The most secure data storage system in the entire galaxy, housing a full backup of thousands of years of data from across the Milky Way. Surely, whatever information is kept inside would be more valuable than any wealth imaginable. Your crew has their eyes set on that data. It won't be easy, of course: the Archive's security is the best in the galaxy, and only the most concise code can be injected without instant lockout. Good luck.

*The team with the shortest code will receive bonus points.*

*This activity is in-person, in the Deepwell Archive.*

## Solution

As described in the challenge, the goal is to write code in as few lines/characters as possible. Stages 1-4 give the main flag on completion.

### Stage 1: ADDING IT UP
Sums all numbers in a list in under 5 lines.

**Sample Solution:**
```python
nums = [1, 2, 3, 4, 5]
print(sum(nums))
```
### Stage 2: BACK2BACK
Reverse a string and concatenate it to the end of itself in under 10 lines.

**Sample Solution:**
```python
s = "python"
print(s + s[::-1])
```

### Stage 3: THE FIBONACCI SEQUENCE
The next task is to write code that will calculate the nth Fibonacci number in under 20 lines.

**Sample Solution:**
```python
def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)

n = 10
print(fib(n))
```

### Stage 4: SORTING IT OUT
The final task is to write code that will sort a list of numbers in under 25 lines. Any sorting algorithm can be used.

**Sample Solution:**
```python
nums = [5, 2, 9, 1, 5, 6]
print(nums.sort())
```

After completion of all 4 stages, a committee member provides the flag of `ATR{sl33k_c0d1ng}` worth 250 points. A second challenge is visible to teams at this point which can be found [here](../../hard/the_deepwell_heist_part_ii_expedited_exfiltration/README.md).

Teams can then optionally try a bonus stage as follows:

### Stage BONUS: QUICKSORT

The bonus task is to write code that will sort a list of numbers using the QuickSort algorithm in under 35 lines.

**Sample Solution:**
```python
def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    left = [x for x in arr[1:] if x < pivot]
    right = [x for x in arr[1:] if x >= pivot]
    return quicksort(left) + [pivot] + quicksort(right)

nums = [5, 2, 9, 1, 5, 6]
print(quicksort(nums))
```

Successful completion of this stage will award the team with a bonus flag of `ATR{m3rg3_n3rd5}` worth 250 points.
