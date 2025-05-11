---
challenge: Clean Code Challanges - File 2
description: Inside a storage closet was found an robotic vacuum cleaner, claimed to be a personal project of Elon Dust’s. Alongside this were files containing hundreds of instructions for the robot. Write programs to decode these instructions and ensure that they’re legitimate.
flag: Automated Flag
scoring: standard(250)
value: 250
category: Medium
authors: Alice Arvidson
---

# Clean Code Challanges - File 2

[Back to Home](../../README.md)

## Points

Medium - 250 points

## Description

Inside a storage closet was found an robotic vacuum cleaner, claimed to be a personal project of Elon Dust’s. Alongside this were files containing hundreds of instructions for the robot. Write programs to decode these instructions and ensure that they’re legitimate.

```python
#********************************************************************************************
# Clean Code Challenges - FILE 2 (MEDIUM)
#
# 
# The second file seems easier to read than the first, however you still press Dust for an explanation. 
# He remarks that it was significantly easier to program the robot if he visualised each room as a grid. 
#
# Each line is then interpreted by the robot as a command to move across the grid in a specified
# direction and number of spaces. 
# For example, the line RIGHT 7 means the robot moves 7 spaces to the right. 
#
# Dust explains that this file is a test containing hundreds of commands to test the robot’s
# movement code and ability to parse large files.
#
# GOAL: 
# Determine the robot's final position by applying the commands in the file.
# Multiply the robot's final vertical position by its horizontal vertical position to get the answer.
# Print the correct number and the challenge will be completed.
#
# RULES:
# 1. Write the program to read the file and compute the right number.
# 2. Ask for help from mentors if you are stuck!
#
#********************************************************************************************
```

## Solution

For this challenge, you need to write a program that reads a list of commands from a file and determines the robot's final position.

You could split each command into a direction and a distance.
Then, you could apply each command to the robot's position and determine the robot's final position.
Finally, multiplying the robot's final vertical position by its horizontal position will give you the answer.

Provided below is the input, sample solution in Python and output:

### Input

See the file [input.txt](input.txt) for full input.
```plaintext
UP 1
UP 4
UP 10
LEFT 7
LEFT 8
DOWN 4
DOWN 5
LEFT 8
...
```

### Sample Solution

```python
with open("input.txt", "r") as f:
  lines = f.readlines()

horizontal = 0
vertical = 0

for line in lines:
  direction, distance = line.strip().split()

  if direction == "UP":
    vertical += int(distance)
  elif direction == "DOWN":
    vertical -= int(distance)
  elif direction == "RIGHT":
    horizontal += int(distance)
  elif direction == "LEFT":
    horizontal -= int(distance)

print(horizontal * vertical)
```

### Output

```plaintext
-975
```
