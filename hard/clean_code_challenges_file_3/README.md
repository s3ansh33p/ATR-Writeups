---
challenge: Clean Code Challanges - File 3
description: Inside a storage closet was found an robotic vacuum cleaner, claimed to be a personal project of Elon Dust’s. Alongside this were files containing hundreds of instructions for the robot. Write programs to decode these instructions and ensure that they’re legitimate.
flag: Automated Flag
scoring: standard(450)
value: 450
category: Hard
authors: Alice Arvidson
---

# Clean Code Challanges - File 3

[Back to Home](../../README.md)

## Points

Hard - 450 points

## Description

Inside a storage closet was found an robotic vacuum cleaner, claimed to be a personal project of Elon Dust’s. Alongside this were files containing hundreds of instructions for the robot. Write programs to decode these instructions and ensure that they’re legitimate.

```python
#********************************************************************************************
# Clean Code Challenges - FILE 3 (HARD)
#
# 
# Upon questioning him about the third file, Dust explains that he works 4 days a week 
# and likes to take his Fridays off knowing all rooms have been cleaned at least once that week. 
# He wants to program the robot to do the same, cleaning each room at least once in each 4 day period. 
#
# He stores the rooms for each day as an 8-bit number, with each bit representing whether
# a room will be cleaned (1 for yes, 0 for no). 
# The robot reads these instructions to know which rooms to clean that day.
#
# GOAL: 
# Determine how many of the 4-day periods instruct the robot to visit every room at least once.
# In other words: How many sets of 4 8-bit numbers have each bit position be 1 at least once?
# Print the correct number and the challenge will be completed
#
# RULES:
# 1. Write the program to read the file and compute the right number.
# 2. Ask for help from mentors if you are stuck!
#
#********************************************************************************************
```

## Solution

For this challenge, you need to write a program that reads a list of 8-bit numbers from a file and determines how many sets of 4 8-bit numbers have each bit position be 1 at least once.

One approach is to OR the first two numbers, then OR the next two numbers, and finally OR the results of the first two ORs. If the result is 255, then the robot has visited every room at least once.

Another approach could be to use a set to keep track of the rooms visited and check if the set has 8 elements, with each element being a number from 0 to 7 (i.e. the indexes of the bits). Only adding to the set if the bit is 1.

Provided below is the input, sample solution in Python and output:

### Input

See the file [input.txt](input.txt) for full input.
```plaintext
11100101
10111011
11001010
11110100
01110010
10011100
00100011
10101110
...
```

### Sample Solution

```python
with open("input.txt", "r") as f:
  lines = f.read().strip().split()

tempArray = []

sum = 0

for i in range(len(lines)):
  if i % 4 == 0:
    tempArray = []

  tempArray.append(int(lines[i], 2))

  if len(tempArray) == 4:
    print(tempArray)
    
    num1 = tempArray[0] | tempArray[1]

    num2 = tempArray[2] | tempArray[3]

    result = num1 | num2

    if result == 255:
      sum += 1

    tempArray = []

print(sum)
```

### Output

```plaintext
56
```
