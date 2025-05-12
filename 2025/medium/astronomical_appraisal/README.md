---
challenge: Astronomical Appraisal
description: "Disguised as a staff member, you receive the following message:\n\n*Congratulations on joining the Intergalactic Mineral Evaluation Team! We already have a project set for you—grading the unique meteors collected from all over the galaxy.*\n*Every single meteor will have observable characteristics such as color, weight, texture, and even radiation levels. With your special scoring system, it is your mission to determine which meteors are rare and which ones are merely space junk!*\n\n*Prepare to:*\n*1. Read data from CSV files*\n*2. Create Python scripts that score every meteor based on their individual characteristics*\n*3. Assess if each meteor meets the threshold score*\n\n*A little bit of programming, problem solving, and utmost intrigue – that's the assignment.*\n\nBest get to work to not arouse suspicion. Good luck."
flag: ATR{373}
scoring: standard(300)
value: 300
category: Medium
authors: Jimmy Yang
---

# Astronomical Appraisal

[Back to Home](../../README.md)

## Points

Medium - 300 points

## Description

Disguised as a staff member, you receive the following message:

*Congratulations on joining the Intergalactic Mineral Evaluation Team! We already have a project set for you—grading the unique meteors collected from all over the galaxy.*
*Every single meteor will have observable characteristics such as color, weight, texture, and even radiation levels. With your special scoring system, it is your mission to determine which meteors are rare and which ones are merely space junk!*

*Prepare to:*
*1. Read data from CSV files*
*2. Create Python scripts that score every meteor based on their individual characteristics*
*3. Assess if each meteor meets the threshold score*

*A little bit of programming, problem solving, and utmost intrigue – that's the assignment.*

Best get to work to not arouse suspicion. Good luck.

```python
import csv

properties = {
    'Colour': {'White': 1, 'Black': 2, 'Grey': 3, 'Brown': 4, 'Red': 5},
    'Origin': {'Earth': 0, 'Mars': 1, 'Moon': 2, 'Venus': 4, '???': 10},
    'Weight': {'Light': 1, 'Medium': 2, 'Heavy': 3, 'Very Heavy': 5},
    'Structure': { 'Amorphous': 1, 'Layered': 2, 'Fibrous': 2, 'Crystalline': 7},
    'Magnetic': {'No': 0, 'Slightly': 1, 'Yes': 2},
    'Texture': {'Rough': 1, 'Grainy': 2, 'Porous': 2, 'Smooth': 4},
    'Hardness': {'Brittle': 0, 'Soft': 1, 'Medium': 2, 'Hard': 3},
    'Reflectivity': {'Low': 1, 'Medium': 2, 'High': 5},
    'Radiation': {'None': 0, 'Low': 1, 'Medium': 2, 'High': 3, 'DANGEROUS': 10},
    'AgeCategory': {'Young': 1, 'Mature': 2, 'Ancient': 5},
    'Rarity': {'Common': 0, 'Uncommon': 1, 'Rare': 2, 'Epic': 3, 'Legendary': 4, 'Mythic': 7, 'Prismatic': 10}
}

GRADE_THRESHOLD = 32  # Score to pass

#TEAMS MUST FINISH THE CODE HERE:
def calculate_score(meteors):
    return
#TEAMS MUST FINISH THE CODE HERE:
def grade_meteors(filename):
    passing_count = 0
    return passing_count

print("\n☄️  Welcome to The Meteor Grading Centre!")

print("\n🔧 Your task: Finish the 'calculate_score(meteors)' and 'grade_meteors(filename)' functions")
print("\n✅ Once you think that you got the correct total, submit your answer to the website!\n")


actual_count = grade_meteors('meteors.csv')
print(f"☄️  {actual_count} meteors passed the grade test!")
```

## Solution

For this challenge, we need to compare each column in the CSV file with the properties dictionary. Each property also has its own dictionary with the possible values and their corresponding scores. Simply sum the scores for each meteor and check if it meets the threshold as seen in the sample solution below.

### Sample Solution

```python
def calculate_score(meteors):
    return sum(properties[prop][meteors[prop]] for prop in properties)

def grade_meteors(filename):
    passing_count = 0
    with open(filename, newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if calculate_score(row) >= GRADE_THRESHOLD:
                passing_count += 1
    return passing_count
```

### Output

```plaintext
373
```
