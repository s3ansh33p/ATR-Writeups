---
challenge: Scrambled Script
description: A scrambled Python script holds an encrypted flag — but nothing is as it seems. Variable names are nonsense, the logic is twisted, and the current output is garbled.\n\nYour task\: reverse the obfuscation, figure out how to extract the hidden flag from the code.\n\nNo guessing. Just clean, careful analysis.
flag: Automated Flag
scoring: standard(400)
value: 400
category: Hard
authors: Sean McGinty
---

# Scrambled Script

[Back to Home](../../README.md)

## Points

Hard - 400 points

## Description

A scrambled Python script holds an encrypted flag—but nothing is as it seems. Variable names are nonsense, the logic is twisted, and the current output is garbled.

Your task: reverse the obfuscation, figure out how to extract the hidden flag from the code.

No guessing. Just clean, careful analysis.

```python
o0oO=0;O0O0o=1;OoO0o=2;
def oO00Oo(oO00OO):oO00oO=''.join([str(O0O0o)if oO00oO=='o'else str(o0oO) for oO00oO in oO00OO]);return int(oO00oO,OoO0o)
def OoO0oO(O0O0o):return[O0O0o[OoO0o:OoO0o+oO00Oo('oOOO')]for OoO0o in range(oO00Oo('O'),len(O0O0o),oO00Oo('oOOO'))]
def o0o0o0O(oO00O,O0o0O,o0O0o0O):return''.join([chr((o000OoO-O0o0O)//o0O0o0O)for o000OoO in oO00O])
def oO0o0():O0oOOo=[oO00Oo(oO00oO)for oO00oO in OoO0oO('oOOOOooooOoOooOooOoOoOOooooooOooooOoooooOooOooOooooOooOoooOoOoOoOooOooooooOOOOooOooOOoooOooOooooooOOOOooooOoOOOooooOoooooooOOOOooooooooo')];return O0oOOo
def O0o0o0o0():oOoOo=oO0o0();O0o0=o0oO;oOoOo0=O0O0o;oOO0O0O=o0o0o0O(oOoOo,O0o0,oOoOo0);print(oOO0O0O)
if __name__=='__main__':O0o0o0o0()
```

## Solution

For this challenge, we need to deobfuscate code to work out what it does. Obfuscation was done by hand for this challenge to combat against automated tools.
A first step we can do is rename functions and parameters which gives us the following code:

```python
o0oO=0;O0O0o=1;OoO0o=2;
def func1(param1):oO00oO=''.join([str(O0O0o)if oO00oO=='o'else str(o0oO) for oO00oO in param1]);return int(oO00oO,OoO0o)
def func2(param2):return[param2[OoO0o:OoO0o+func1('oOOO')]for OoO0o in range(func1('O'),len(param2),func1('oOOO'))]
def func3(param3,param4,param5):return''.join([chr((o000OoO-param4)//param5)for o000OoO in param3])
def func4():O0oOOo=[func1(oO00oO)for oO00oO in func2('oOOOOooooOoOooOooOoOoOOooooooOooooOoooooOooOooOooooOooOoooOoOoOoOooOooooooOOOOooOooOOoooOooOooooooOOOOooooOoOOOooooOoooooooOOOOooooooooo')];return O0oOOo
def func5():oOoOo=func4();O0o0=o0oO;oOoOo0=O0O0o;oOO0O0O=func3(oOoOo,O0o0,oOoOo0);print(oOO0O0O)
if __name__=='__main__':func5()
```

We'll change the variable name on line 3 in the list comprehension. It is important that we do this first, and don't do a find and replace all as this has the same variable name as one of the numbers on line 1.

```python
# def func2(param2):return[param2[OoO0o:OoO0o+func1('oOOO')]for OoO0o in range(func1('O'),len(param2),func1('oOOO'))]
def func2(param2):return[param2[var1:var1+func1('oOOO')]for var1 in range(func1('O'),len(param2),func1('oOOO'))]
```

Now let's rename the variables on the first line.

```python
const0=0;const1=1;const2=2;
def func1(param1):oO00oO=''.join([str(const1)if oO00oO=='o'else str(const0) for oO00oO in param1]);return int(oO00oO,const2)
def func2(param2):return[param2[var1:var1+func1('oOOO')]for var1 in range(func1('O'),len(param2),func1('oOOO'))]
def func3(param3,param4,param5):return''.join([chr((o000OoO-param4)//param5)for o000OoO in param3])
def func4():O0oOOo=[func1(oO00oO)for oO00oO in func2('oOOOOooooOoOooOooOoOoOOooooooOooooOoooooOooOooOooooOooOoooOoOoOoOooOooooooOOOOooOooOOoooOooOooooooOOOOooooOoOOOooooOoooooooOOOOooooooooo')];return O0oOOo
def func5():oOoOo=func4();O0o0=const0;oOoOo0=const1;oOO0O0O=func3(oOoOo,O0o0,oOoOo0);print(oOO0O0O)
if __name__=='__main__':func5()
```

We'll continue renaming other variables.

```python
const0=0;const1=1;const2=2;
def func1(param1):var0=''.join([str(const1)if var0=='o'else str(const0) for var0 in param1]);return int(var0,const2)
def func2(param2):return[param2[var1:var1+func1('oOOO')]for var1 in range(func1('O'),len(param2),func1('oOOO'))]
def func3(param3,param4,param5):return''.join([chr((var2-param4)//param5)for var2 in param3])
def func4():var4=[func1(var3)for var3 in func2('oOOOOooooOoOooOooOoOoOOooooooOooooOoooooOooOooOooooOooOoooOoOoOoOooOooooooOOOOooOooOOoooOooOooooooOOOOooooOoOOOooooOoooooooOOOOooooooooo')];return var4
def func5():var8=func4();var6=const0;var5=const1;var7=func3(var8,var6,var5);print(var7)
if __name__=='__main__':func5()
```

Now let's format things a bit better.

```python
const0=0
const1=1
const2=2

def func1(param1):
    =''.join([str(const1) if var9=='o' else str(const0) for var9 in param1])
    return int(var0,const2)

def func2(param2):
    return[param2[var1:var1+func1('oOOO')] for var1 in range(func1('O'), len(param2), func1('oOOO'))]

def func3(param3,param4,param5):
    return''.join([chr((var2-param4)//param5) for var2 in param3])

def func4():
    var4=[func1(var3) for var3 in func2('oOOOOooooOoOooOooOoOoOOooooooOooooOoooooOooOooOooooOooOoooOoOoOoOooOooooooOOOOooOooOOoooOooOooooooOOOOooooOoOOOooooOoooooooOOOOooooooooo')]
    return var4

def func5():
    var8=func4()
    var6=const0
    var5=const1
    var7=func3(var8,var6,var5)
    print(var7)

if __name__=='__main__':
    func5()
```

Let's try adding a print statement after `func4()` to see what is going on.

```python
def func5():
    var8=func4()
    print(var8) # OUR CODE
```

It looks like the string is being decoded into integers:

```bash
[135, 173, 169, 251, 223, 109, 237, 213, 111, 195, 103, 111, 195, 209, 239, 225, 255]
```

You may have noticed that there is a custom binary encoding scheme being used where instead of `0` and `1`, the letters `'o'` and `'O'` are used.

```python
def func1(param1):
    var0=''.join([str(const1) if var9=='o' else str(const0) for var9 in param1])
    return int(var0,const2)
# swap in our const0,1,2 in and clean up some rename a bit more:
def custom_binary_to_decimal(custom_binary):
    binary=''.join(['1' if char=='o' else '0' for char in custom_binary])
    return int(binary,2) # this is converting a binary string to an integer
```

You don't need to work that out to get to the solution however. The main discovery is the decimal array. func3 is where it gets interesting, and currently we are calling it with the decimal array, and two numbers `0` and `1`.

```python
    var7=func3(var8, 0, 1)
```

Let's look at func3 a bit closer and we can renamed `param3` to `decimal_array` to help us

```python
def func3(decimal_array,param4,param5):
    return''.join([chr((var2-param4)//param5) for var2 in decimal_array])
```

Each of numbers in the array are being shifted by `param4` and divided by `param5`. This is a major discovery!

We know that the flag starts with `ATR{` and `A` is `65` in ASCII. So we can work out what the values of `param4` and `param5` are.

`65 = (135 - param4) // param5`

This can be solved upon visual inspection, or you could write a simple for loop from 1-10 for each.

Ultimately, we find that `param4 = 5`, `param5 = 2`. Noting that // is an integer division, `param4 = 4` would also work.

So now let's use values `5` and `2` in the function.

```python
    var7=func3(var8,5,2)
    print(var7) # ATR{m4th5_15_fun}
```

And we have the flag of `ATR{m4th5_15_fun}`

For those curious, this was the helper code before obfuscation:

```python
def encode_flag(flag, offset, multiplier):
    return [(ord(c) * multiplier) + offset for c in flag]

def decode_flag(numbers, offset, multiplier):
    return ''.join([chr((n - offset) // multiplier) for n in numbers])

def main():
    flag = "ATR{m4th5_15_fun}"
    offset = 5
    multiplier = 2
    
    encoded = encode_flag(flag, offset, multiplier)
    print(encoded) # [135, 173, 169, 251, 223, 109, 237, 213, 111, 195, 103, 111, 195, 209, 239, 225, 255]

    recovered = decode_flag(encoded, offset, multiplier)
    print(recovered)

if __name__ == "__main__":
    main()
```
