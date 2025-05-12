---
challenge: Point of Fail
description: "Disguised as a staff member, you notice a commotion at the cafeteria register. The code's been corrupted, become riddled with errors and the total is way off. Fix it up, submit the correct total, and you'll gain trust amongst the staff. Maybe someone will trust you enough to ask you to fix more sensitive systems, or even share their part of the safe code?"
flag: ATR{551.08}
scoring: standard(100)
value: 100
category: Easy
authors: Jimmy Yang
---

# Point of Fail

[Back to Home](../../README.md)

## Points

Easy - 100 points

## Description

Disguised as a staff member, you notice a commotion at the cafeteria register. The code's been corrupted, become riddled with errors and the total is way off. Fix it up, submit the correct total, and you'll gain trust amongst the staff. Maybe someone will trust you enough to ask you to fix more sensitive systems, or even share their part of the safe code?

```python
import hashlib

# === Static Cart: Predefined Items with Fixed Quantities ===
cart = [
    {"name": "Apple", "price": 1.50, "quantity": 2},
    {"name": "Bread", "price": 2.80, "quantity": 1},
    {"name": "Milk", "price": 3.20, "quantity": 3},
    {"name": "Cheese", "price": 4.75, "quantity": 2},
    {"name": "Chocolate", "price": 6.90, "quantity": 1},
    {"name": "Banana", "price": 0.50, "quantity": 4},
    {"name": "Eggs", "price": 3.00, "quantity": 2},
    {"name": "Pasta", "price": 1.25, "quantity": 5},
    {"name": "Cereal", "price": 4.50, "quantity": 1},
    {"name": "Yogurt", "price": 1.20, "quantity": 3},
    {"name": "Juice", "price": 2.50, "quantity": 2},
    {"name": "Coffee", "price": 5.00, "quantity": 1},
    {"name": "Tea", "price": 3.20, "quantity": 1},
    {"name": "Sugar", "price": 1.80, "quantity": 2},
    {"name": "Salt", "price": 0.90, "quantity": 6},
    {"name": "Pepper", "price": 1.10, "quantity": 4},
    {"name": "Honey", "price": 4.80, "quantity": 1},
    {"name": "Jam", "price": 2.20, "quantity": 3},
    {"name": "Peanut Butter", "price": 3.50, "quantity": 2},
    {"name": "Chips", "price": 2.00, "quantity": 5},
    {"name": "Soda", "price": 1.75, "quantity": 2},
    {"name": "Water", "price": 0.99, "quantity": 7},
    {"name": "Cookies", "price": 3.25, "quantity": 2},
    {"name": "Crackers", "price": 2.10, "quantity": 4},
    {"name": "Soup", "price": 1.95, "quantity": 1},
    {"name": "Noodles", "price": 1.30, "quantity": 6},
    {"name": "Mustard", "price": 1.60, "quantity": 4},
    {"name": "Ketchup", "price": 1.85, "quantity": 3},
    {"name": "Mayonnaise", "price": 2.75, "quantity": 2},
    {"name": "Pickles", "price": 2.65, "quantity": 2},
    {"name": "Cucumber", "price": 0.75, "quantity": 5},
    {"name": "Carrot", "price": 0.55, "quantity": 6},
    {"name": "Lettuce", "price": 1.15, "quantity": 3},
    {"name": "Spinach", "price": 1.45, "quantity": 2},
    {"name": "Broccoli", "price": 1.35, "quantity": 4},
    {"name": "Cauliflower", "price": 1.55, "quantity": 2},
    {"name": "Peas", "price": 1.05, "quantity": 5},
    {"name": "Corn", "price": 0.85, "quantity": 6},
    {"name": "Green Beans", "price": 1.25, "quantity": 4},
    {"name": "Garlic", "price": 0.65, "quantity": 8},
    {"name": "Ginger", "price": 0.95, "quantity": 3},
    {"name": "Orange", "price": 0.90, "quantity": 6},
    {"name": "Grapes", "price": 2.25, "quantity": 2},
    {"name": "Strawberries", "price": 3.75, "quantity": 1},
    {"name": "Blueberries", "price": 4.00, "quantity": 3},
    {"name": "Raspberries", "price": 3.50, "quantity": 2},
    {"name": "Blackberries", "price": 3.25, "quantity": 3},
    {"name": "Pineapple", "price": 2.50, "quantity": 2},
    {"name": "Mango", "price": 1.95, "quantity": 5},
    {"name": "Kiwi", "price": 0.80, "quantity": 8},
    {"name": "Peach", "price": 1.10, "quantity": 4},
    {"name": "Pear", "price": 1.20, "quantity": 5},
    {"name": "Plum", "price": 0.75, "quantity": 7},
    {"name": "Cherry", "price": 2.80, "quantity": 2},
    {"name": "Watermelon", "price": 3.00, "quantity": 1},
    {"name": "Cantaloupe", "price": 2.20, "quantity": 4},
    {"name": "Honeydew", "price": 2.10, "quantity": 2},
    {"name": "Pomegranate", "price": 3.40, "quantity": 3},
    {"name": "Avocado", "price": 1.75, "quantity": 5},
    {"name": "Coconut", "price": 2.30, "quantity": 6},
    {"name": "Almonds", "price": 5.50, "quantity": 1},
    {"name": "Walnuts", "price": 4.75, "quantity": 2},
    {"name": "Cashews", "price": 6.00, "quantity": 3},
    {"name": "Pistachios", "price": 5.25, "quantity": 4},
    {"name": "Raisins", "price": 2.15, "quantity": 7},
    {"name": "Dates", "price": 3.80, "quantity": 2},
    {"name": "Prunes", "price": 2.90, "quantity": 4},
    {"name": "Granola", "price": 3.60, "quantity": 3},
    {"name": "Oatmeal", "price": 2.40, "quantity": 5},
    {"name": "Syrup", "price": 3.10, "quantity": 2},
    {"name": "Hot Sauce", "price": 1.50, "quantity": 4},
    {"name": "Soy Sauce", "price": 1.80, "quantity": 2},
    {"name": "BBQ Sauce", "price": 2.45, "quantity": 3},
    {"name": "Salsa", "price": 2.30, "quantity": 1},
    {"name": "Tortilla Chips", "price": 2.20, "quantity": 3},
    {"name": "Popcorn", "price": 1.40, "quantity": 5},
    {"name": "Pretzels", "price": 1.90, "quantity": 2},
    {"name": "Trail Mix", "price": 3.30, "quantity": 3},
    {"name": "Protein Bar", "price": 2.50, "quantity": 6},
    {"name": "Candy", "price": 1.25, "quantity": 7},
    {"name": "Gum", "price": 0.99, "quantity": 10},
    {"name": "Mints", "price": 1.10, "quantity": 3},
    {"name": "Ice Cream", "price": 4.50, "quantity": 1},
]

# THE TEAM MUST FIX THIS PART OF THE CODE
def corrupted_total(cart):
    total = 0
    '''
    for I in range(len[Cart]):
        p = cart[i]["prїce"]
        q = cart[i]["quantїty"]

        total += p + q  
    '''
    return round(total, 2)

def main():

    print("\n🛒 Welcome to The Kiosk!")

    print("\n🔧 Your task: Fix the 'corrupted_total()' function in the code.")
    print("\n✅ Once you think that you got the correct total, submit your answer to the website!")
    print("\n When you are ready, remove the block comment from the 'corrupted_total()' function to begin!")

    displayed = corrupted_total(cart)
    print(f"💰 Kiosk Says: ${displayed}")

if __name__ == "__main__":
    main()
```

## Solution

When first trying to run the `corrupted_total()` function, you'll run into an error:

```
Traceback (most recent call last):
  File "/box/submission/user.py", line 112, in <module>
    main()
  File "/box/submission/user.py", line 108, in main
    displayed = corrupted_total(cart)
  File "/box/submission/user.py", line 93, in corrupted_total
    for I in range(len[Cart]):
NameError: name 'Cart' is not defined. Did you mean: 'cart'?
```

We need to clean up a few issues in the code. First we'll fix up the variable names.

```python
def corrupted_total(cart):
    total = 0
    for i in range(len[cart]):
        p = cart[i]["price"]
        q = cart[i]["quantity"]

        total += p + q  
    return round(total, 2)
```

When running the code again, we get a different error:

```
Traceback (most recent call last):
  File "/box/submission/user.py", line 112, in <module>
    main()
  File "/box/submission/user.py", line 108, in main
    displayed = corrupted_total(cart)
  File "/box/submission/user.py", line 93, in corrupted_total
    for i in range(len[cart]):
TypeError: 'builtin_function_or_method' object is not subscriptable
```

We need to change `len[cart]` to `len(cart)`.

```python
def corrupted_total(cart):
    total = 0
    for i in range(len(cart)):
        p = cart[i]["price"]
        q = cart[i]["quantity"]

        total += p + q  
    return round(total, 2)
```

We get a successful run, but the total is incorrect:

```
💰 Kiosk Says: $484.48
```

We need to change the `total += p + q` to `total += p * q` to get the correct total.

```python
def corrupted_total(cart):
    total = 0
    for i in range(len(cart)):
        p = cart[i]["price"]
        q = cart[i]["quantity"]

        total += p * q  
    return round(total, 2)
```

Now we get the correct total, `551.08`, which we can submit as the flag:

```
💰 Kiosk Says: $551.08
```
