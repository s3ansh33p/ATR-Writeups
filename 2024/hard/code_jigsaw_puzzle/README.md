---
challenge: Code Jigsaw Puzzle
description: In 5 minutes, participants are given code snippets to make methods/algorithms to get the desired output or behaviour. You will have 5 minutes to get all the algorithms sorted to reveal the flag, or if you struggle, the flag will be given to you after 3 attempts.
flag: ATR{ju5t1n_p4n}
scoring: decay(500,200,10)
value: 500
category: Hard
authors: Justin Pan, Cindy Lawrence
---

[Back to Home](../../README.md)

# Code Jigsaw Puzzle

## Points

Hard - 500 points

## Description

In 5 minutes, participants are given code snippets to make methods/algorithms to get the desired output or behaviour. You will have 5 minutes to get all the algorithms sorted to reveal the flag, or if you struggle, the flag will be given to you after 3 attempts.

## Solution

Participants are given a number of cutouts, each representing one line of code. Some are used in the final solution, whilst some are not. Participants are required to make a piece snippet of pseudocode that will provide the desired output. In a certain amount of time, if participants are able to complete x number of code snippets, they will be rewarded a corresponding number of points. 

Key
```diff
+ indicates segments that should be included in the final solution
- indicates fake segments to throw participants off.
```

### Code Snippet 1
**Name:** Searching through the building security access door Logs

**Description:** Sorting a csv file with insertion sort and then print out the first name 

**Link to Narrative:** Seeing who came into the room at that specific time of her death

**Difficulty Level:** Intermediate

**Code:**

```diff
+   BEGIN
+       LET logFile[] BE logs.csv
       
+       FOR i = 1 to logFile.LENGTH; increment
+           key-> logFile[i].TIME
+           j = i - 1 
-           i = i + 1

+           WHILE j GREATER OR EQUAL TO 0 AND logFile[i].TIME GREATER THAN key 
+               logFile.TIME[j + 1] = logFile.TIME[j]
+               j = j - 1
+           END WHILE
-           logFile[i + 1] = key
+           logFile[j + 1] = key
+       END FOR
            
+       PRINT logFile.NAME[0]
-       PRINT logFile.NAME[1]
+   END
```

### Code Snippet 2
**Name:** Find the max voltage

**Description:** Given the Array, find the highest number in the array.

**Link to Narrative:** Find the highest voltage numbers the users experienced in the set of numbers derived from the experiments. From this, we can see how the CEO died

**Difficulty Level:** Easy

**Code:**

```diff
+   BEGIN 
+       LET voltList ARRAY OF INTEGERS -> {60, 103, 233, 200, 10, 243, 150, 140, 201, 170}
+       LET maxVolt -> 0
            
+       FOR i = 0 to 9; increment
-       FOR i = 0 to voltList.LENGTH
+           IF voltList[i] BIGGER THAN maxVolt THEN
-               voltList[i] -> maxVolt
+               maxVolt -> voltList[i]
+           ENDIF
+       END FOR

+       PRINT "The highest voltage to result in a safe outcome is... " + maxVolt
+   END
```