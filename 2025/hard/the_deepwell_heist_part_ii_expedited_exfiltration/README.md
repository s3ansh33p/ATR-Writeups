---
challenge: The Deepwell Heist Part II: Expedited Exfiltration
description: "You've managed to infiltrate the most secure server in the galaxy. Your presence is known however, and any data you can access is being erased within a matter of seconds. Keep your eyes sharp and gather what data you can before access is lost for good.\n\n*This activity is in-person, in the Deepwell Archive.*"
flag: ATR{m3m0r153_m3}
scoring: subflags(300, 350)
value: 650
category: Hard
authors: Alice Arvidson
---

# The Deepwell Heist Part II: Expedited Exfiltration

[Back to Home](../../README.md)

## Points

Hard - 650 points

## Description

You've managed to infiltrate the most secure server in the galaxy. Your presence is known however, and any data you can access is being erased within a matter of seconds. Keep your eyes sharp and gather what data you can before access is lost for good.

*This activity is in-person, in the Deepwell Archive.*

## Solution

This challenge is visible to teams after completing [Part I](../../medium/the_deepwell_heist_part_i_invisible_infiltration/README.md).

Based on [Code Memory (2024)](../../../2024/medium/code_memory/README.md), participants are given a series of code snippets to memorize. The challenge is to remember as many lines of code as possible before they disappear. Can choose either Python or Java.

### Python Code Snippets

```python
def sumOfTwo(firstNum, secondNum):
    total = firstNum + secondNum
    return total
```

```python
def fibonacciSum(inNum):
    firstNum, secondNum = 1, 1
    count = 0
    total = 0

    while count < inNum:
      total += firstNum
      nextNum = firstNum + secondNum
      firstNum = secondNum
      secondNum = nextNum
      count += 1
    return total
```

```python
def binarySearch(nums, target):
    left = 0
    right = len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if target == nums[mid]:
            return mid
        elif target < nums[mid]:
            right = mid - 1
        else:
            left = mid + 1
    return -1
```

### Java Code Snippets

```java
public static int sumOfTwo(int firstNum, int secondNum){
    int total = firstNum + secondNum;
    return total;
}
```

```java
public static int fibonacciSum(int inNum){
    int firstNum = 1
    int secondNum = 1
    int nextNum;
    int count = 0;
    int total = 0;

    while (count < inNum){
        total += firstNum;
        nextNum = firstNum + secondNum;
        firstNum = secondNum;
        secondNum = nextNum;
        count += 1;
    }
    return total;
}
```

```java
public static int binarySearch(int[] nums, int target){
    int left = 0, right = nums.length - 1;
    while (left <= right)
    {
        int mid = (left + right) / 2;
        if (target == nums[mid]) {
            return mid;
        } else if (target < nums[mid]) {
            right = mid - 1;
        } else {
            left = mid + 1;
        }
    }
    return -1;
}
```


After completion of all 3 snippets, a committee member provides the flag of `ATR{m3m0r153_m3}` worth 300 points. 

Teams can then optionally try a bonus challenge as follows:

### Python Code Snippet

```python
def split(matrix):
    row, col = matrix.shape
    row2, col2 = row // 2, col // 2
    return matrix[:row2, :col2], matrix[:row2, col2:], matrix[row2:, :col2], matrix[row2:, col2:]

def strassen(x, y):
    if len(x) == 1:
        return x * y

    a, b, c, d = split(x)
    e, f, g, h = split(y)

    p1 = strassen(a, f - h)
    p2 = strassen(a + b, h)
    p3 = strassen(c + d, e)
    p4 = strassen(d, g - e)
    p5 = strassen(a + d, e + h)
    p6 = strassen(b - d, g + h)
    p7 = strassen(a - c, e + f)

    c11 = p5 + p4 - p2 + p6
    c12 = p1 + p2
    c21 = p3 + p4
    c22 = p1 + p5 - p3 - p7

    c = np.vstack((np.hstack((c11, c12)), np.hstack((c21, c22))))

    return c
```

### Java Code Snippet

```java
public static int[][] Strassen(int[][] A, int[][] B) {
    int n = A.length;
    int[][] returnMatrix = new int[n][n];
    if (n == 1) {
        returnMatrix[0][0] = A[0][0] * B[0][0];
    } else {
        int[][] A11 = new int[n / 2][n / 2];
        int[][] A12 = new int[n / 2][n / 2];
        int[][] A21 = new int[n / 2][n / 2];
        int[][] A22 = new int[n / 2][n / 2];
        int[][] B11 = new int[n / 2][n / 2];
        int[][] B12 = new int[n / 2][n / 2];
        int[][] B21 = new int[n / 2][n / 2];
        int[][] B22 = new int[n / 2][n / 2];

        int[][] M1 = Strassen(add(A11, A22), add(B11, B22));
        int[][] M2 = Strassen(add(A21, A22), B11);
        int[][] M3 = Strassen(A11, sub(B12, B22));
        int[][] M4 = Strassen(A22, sub(B21, B11));
        int[][] M5 = Strassen(add(A11, A12), B22);
        int[][] M6 = Strassen(sub(A21, A11), add(B11, B12));
        int[][] M7 = Strassen(sub(A12, A22), add(B21, B22));

        int[][] C11 = add(sub(add(M1, M4), M5), M7);
        int[][] C12 = add(M3, M5);
        int[][] C21 = add(M2, M4);
        int[][] C22 = add(sub(add(M1, M3), M2), M6);

        join(C11, returnMatrix, 0, 0);
        join(C12, returnMatrix, 0, n / 2);
        join(C21, returnMatrix, n / 2, 0);
        join(C22, returnMatrix, n / 2, n / 2);
    }
    return returnMatrix;
}
```

Successful completion of this challenge will award the team with a bonus flag of `ATR{5tr4553n_0ut}` worth 350 points.
