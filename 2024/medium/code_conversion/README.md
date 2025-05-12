---
challenge: Code Conversion
description: Pseudocode for a Brainsave algorithm was found in Dr Curing's files, but the local source code cannot be found. \nImplement the algorithm using different coding languages and uncover the truth.
flag: ATR{M4J0R_H34D4CH3}
scoring: subflags(100, 200, 100)
value: 400
category: Medium
authors: Alice Arvidson
---

# Code Conversion

[Back to Home](../../README.md)

## Points

Medium - 400 points

## Description

Pseudocode for a Brainsave algorithm was found in Dr Curing's files, but the local source code cannot be found. 

Implement the algorithm using different coding languages and uncover the truth.

## Solution

The folllowing pseudocode algorithm is provided - running through a 1D array of neurons and decoding an instruction that the chip then runs.

```js
BEGIN SECRET_PROGRAM
    numLogs ← GET INTEGER INPUT FROM USER
    justineBrainsaveLog ← INTEGER ARRAY OF SIZE numLogs
    safetyThreshold ← 75

    FOR i ← 0 TO numLogs-1 INCREMENT 1 DO

        voltage ← (i + 47)*77 MODULO 103

        IF voltage GREATER THAN safetyThreshold THEN

            voltage ← safetyThreshold

        END IF

        justineBrainsaveLog[i] ← voltage

    END FOR

END 
```

### Python

Awards main flag `ATR{M4J0R_H34D4CH3}` for 100 points. Sample solution:

```python
numLogs = int(input("Number of logs?"))
justineBrainsaveLog = []
safetyThreshold = 75

for i in range(numLogs):
    voltage = (i + 47)*77 % 103

    if voltage > safetyThreshold:
        voltage = safetyThreshold

    justineBrainsaveLog.append(voltage)

```

### Java

Awards flag `ATR{C4FF31N4T3D}` for 200 points and main flag. Sample solution:

```java
import java.util.Scanner;

class Main
{
    public static void main(String[] args) 
    {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Number of logs?");

        int numLogs = scanner.nextInt();

        int[] justineBrainsaveLog = new int[numLogs];
        int safetyThreshold = 75;

        for (int i = 0; i < numLogs; i++)
        {
            int voltage = (i + 47) * 77 % 103;

            if (voltage > safetyThreshold)
            {
                voltage = safetyThreshold;
            }

            justineBrainsaveLog[i] = voltage;
        }
    }
}
```

### C

Awards flag `ATR{M3M0R13S_L34K3D}` and other flags for total of 400 points. Sample solution:

```c
#include <stdio.h>
#include <stdlib.h>

int main(void)
{
    int numLogs; 

    printf("Number of logs? \n");

    scanf("%d", &numLogs);

    justineBrainsaveLog = (int*)malloc(numLogs * sizeof(int));

    int safetyThreshold = 75;

    for (int i = 0; i < numLogs; i++)
    {
        int voltage = (i + 47) * 77 % 103;

        if (voltage > safetyThreshold)
        {
            voltage = safetyThreshold;
        }

        justineBrainsaveLog[i] = voltage;
    }

    free(justineBrainsaveLog);
}
```