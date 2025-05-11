---
challenge: Code Relay
description: A hacker is trying to infiltrate our headquarters and spread confidential information regarding Justina Panetta. They're sending out parts of code to recombine inside of our database to wreak havoc. Are they the public press? Our rival company? Whoever they are, you must work in pairs to stop them at all cost.
flag: ATR{5U5P1C10U5_PR0MP7}
scoring: subflags(300, 300, 200)
value: 800
category: Medium
authors: Stanley Zhong, Memphis Marshall (2023)
---

# Code Relay

[Back to Home](../../README.md)

## Points

Medium - 800 points

## Description

A hacker is trying to infiltrate our headquarters and spread confidential information regarding Justina Panetta. They're sending out parts of code to recombine inside of our database to wreak havoc. Are they the public press? Our rival company? Whoever they are, you must work in pairs to stop them at all cost.

## Solution

Participants will work together as a single group to complete as many questions as possible in 5 minutes. They can work as one, delegate tasks to an individual, or a mixture of combinations. These can be completed in Java or Python.

The problems are split into two groups: Tier 1 and Tier 2 which are based on their bracket. The problems are as follows:

### Tier 1

#### Question 1

Given an array, return the median value of the array (You can use Numpy)

```python
def question1(inArray):
    np.sort(inArray)
    return inArray[len(inArray)/2]
```

#### Question 2

Given an integer, print the sum of all the numbers leading up to the number:

```python
def question2_1(inNum):
    return (inNum(inNum + 1) / 2)
```

Alternative sample solution

```python
def question2_2(inNum):
    total = 0
    for i in range(inNum):
        total += i
    return total
```

#### Question 3

Given a string, return the number of times each vowel appears (Assume string is all lower case)

```python
def question3(inString):
    totalVowels = {}
    for i in inString:
        if i not in totalVowels:
            totalVowels[i] = 0
        else:
            totalVowels[i] += 1

    return totalVowels["a"], totalVowels["e"], totalVowels["i"], totalVowels["o"], totalVowels["u"]
```

### Tier 2

#### Question 1

For all numbers leading to a given an integer, print "Fizz" if the number is divisible by 5, or else print the number

```python
def question1(inNum):
    for i in range(inNum):
        if i % 5 == 0:
            print("Fizz")
        else:
            print(i)
```

#### Question 2

Print the times tables grid from 1 to 10 [Please make it easy for us to read :) ]

```python
def question2():
    for i in range(1, 11):
        for j in range(1, 11):
            print(str(i * j) + " ", end="")
        print("")
```

#### Question 3

Calculate the factorial of a given number

```python
def factorial(n):
  if n == 0 or n == 1:
    return 1
  else:
    return n * factorial(n - 1)
```

For each question they complete, they will receive a flag in the following order:
- `ATR{5U5P1C10U5_PR0MP7}` - 300 points (main flag)
- `ATR{S4B0T4G3D_C0D3}` - 300 points
- `ATR{3RR0R_F0UND}` - 200 points

Note: the weighting of points was not done properly in the scoring section. Each flag should be worth 100 points each. Teams who placed 2nd through 5th all did this challenge, although the overall winning team did not.