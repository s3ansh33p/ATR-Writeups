---
challenge: Clean Code Challanges - File 1
description: Inside a storage closet was found an robotic vacuum cleaner, claimed to be a personal project of Elon Dust’s. Alongside this were files containing hundreds of instructions for the robot. Write programs to decode these instructions and ensure that they’re legitimate.
flag: Automated Flag
scoring: standard(100)
value: 100
category: Easy
authors: Alice Arvidson
---

# Clean Code Challanges - File 1

[Back to Home](../../README.md)

## Points

Easy - 100 points

## Description

Inside a storage closet was found an robotic vacuum cleaner, claimed to be a personal project of Elon Dust’s. Alongside this were files containing hundreds of instructions for the robot. Write programs to decode these instructions and ensure that they’re legitimate.

```python
#********************************************************************************************
# Clean Code Challenges - FILE 1 (EASY)
#
# 
# The first file found with Dust's robot was a series of numbers, both positive and negative.
# Dust claims that it was a test input file to test the robot's ability to filter out data.
# The robot should run through the list and only sum the positive numbers, ignoring the negative junk data.
#
# GOAL: 
# Read the file and get the list of numbers from it.
# Find the sum of all positive numbers from the list!
# Print the correct number and the challenge will be completed.
#
# RULES:
# 1. Write the program to sum only positive numbers and print the correct output.
# 2. Ask for help from mentors if you are stuck!
#
#********************************************************************************************
```

## Solution

For this challenge, you need to write a program that reads a list of numbers from a file and finds the sum of all positive numbers from the list.

The program should print the correct sum. Provided below is the input, sample solution in Python and output:

### Input

```plaintext
[-12, -5, -15, -17, -20, 16, 2, -16, 11, -13]
```

### Sample Solution

```python
f = open("input.txt", "r")

numbers = [int(num) for num in f.read().strip("[]").split(",")]

sum_positive = sum(num for num in numbers if num > 0)
print(sum_positive)
```

### Output

```plaintext
29
```
