---
challenge: The Great Escape
description: "The Museum Sector stretches on forever. Endless halls and corridors, concrete and titanium as far as one can imagine, smothering the space between the stars. Was this really built by humans? Regardless, you need to figure out the most important part of any heist: the escape plan. \n\nYou have access to a data map of the sector, but it’s encoded as a series of numbered rooms and connected hallways. Thankfully, you have insider intel, of course. Consider a line from the data map: “0,X,1,2”. The first column means current room number, and the rest of the columns represent connected rooms. X means no connected room. In this example, it means room 0 has connections to rooms 1 and 2. Note that the rooms don’t interconnect, and there is only one unique way to get to each room. In this example, room 2 is only reached from room 0.\n\nYour goal is to find a route all the way to room “E”, the escape point. Then, to sum all the room numbers that make up that route and submit that to your crew."
flag: ATR{19939}
scoring: standard(600)
value: 600
category: Hard
authors: Alice Arvidson
---

# The Great Escape

[Back to Home](../../README.md)

## Points

Hard - 600 points

## Description

The Museum Sector stretches on forever. Endless halls and corridors, concrete and titanium as far as one can imagine, smothering the space between the stars. Was this really built by humans? Regardless, you need to figure out the most important part of any heist: the escape plan. 

You have access to a data map of the sector, but it’s encoded as a series of numbered rooms and connected hallways. Thankfully, you have insider intel, of course. Consider a line from the data map: “0,X,1,2”. The first column means current room number, and the rest of the columns represent connected rooms. X means no connected room. In this example, it means room 0 has connections to rooms 1 and 2. Note that the rooms don’t interconnect, and there is only one unique way to get to each room. In this example, room 2 is only reached from room 0.

Your goal is to find a route all the way to room “E”, the escape point. Then, to sum all the room numbers that make up that route and submit that to your crew.

```python
# Class representing a Room in the Museum Sector
# Each Room has a series of connecting corridors, like how trees have leaves
# The primary purpose of the class is to search for specific Rooms, and return the path to it
class Room():
# Room constructor, with an optional name and list of branches
    def __init__(self, name="Root", branches=None):
        self.name = name
        self.branches = []

        if branches is not None:
            for branch in branches:
                self.add_branch(self, branch)

    #  A basic way of representing a room and its branches as a string
    def __repr__(self):
        return f"{self.name} \n({self.branches})"
                                                                                                
    # Add a new branch to another Room
    def add_branch(self, branch):
        assert isinstance(branch, Room)
        self.branches.append(branch)

    # Search for the given target Room and return the path to it
    def search(self, target):
        path = [self.name]

        # The map's routing algorithm has been lost!
        # It was a function that finds the path to a target room
        # It should return the path, whether it be a list of room numbers or sum of them

        return path

# Read mazemap.csv as a list of strin
def readMap():
    with open("escape_datamap.csv", "r") as file:
        map_data = file.readlines()

        return map_data

# Main function for handling the map 
def main():
    map_data = readMap()

    root = Room("0")

    # Find the path from Room 0 to Room E
    escape_path = root.search("E")

    # The correct output will be the sum of room numbers in the path
    print(escape_path)


if __name__ == "__main__":
    main()
```

## Solution

A basic tree structure is used to represent the rooms and their connections to guide students in the right direction. The search function needs to be implemented that traverses the tree structure recursively.

The tree itself also needs to be built from the CSV file. The first column of the CSV file is the parent room, and the rest are the children rooms. Create a new `Room` object for each room as you walk through the CSV file. Similarly, you'll need to add branches to the parent room as you go. Data can be stored in a dictionary for quick access via the key which is the room number.

### Sample Solution

```python
# Class representing a Room in the Museum Sector
# Each Room has a series of connecting corridors, like how trees have leaves
# The primary purpose of the class is to search for specific Rooms, and return the path to it
class Room():
    # Room constructor, with an optional name and list of branches
    def __init__(self, name="Root", branches=None):
        self.name = name
        self.branches = []

        if branches is not None:
            for branch in branches:
                self.add_branch(self, branch)

    # A basic way of representing a room and its branches as a string
    def __repr__(self):
        return f"{self.name} \n({self.branches})"
    
    # Add a new branch to another Room
    def add_branch(self, branch):
        assert isinstance(branch, Room)
        self.branches.append(branch)

    # Search for the given target Room and return the path to it
    def search(self, target):
        path = [self.name]

        # Search for target in each available branch
        for branch in self.branches:
            rest_of_path = branch.search(target)

            # This condition is only true if the branch leads to the exit, and so its path will always be the correct one
            if rest_of_path is not None:
                path.extend(rest_of_path)

        # Base case where target is found, or case where node is on the correct path
        if (self.name == target) or (len(path) > 1):
            return path
        
        # If node is not on the correct path, return none
        else:
            return None

# Read escape_datamap.csv as a list of strings
def readMap():
    with open("escape_datamap.csv", "r") as file:
        map_data = file.readlines()

        return map_data

# Main function for handling the map 
def main():
    map_data = readMap()

    # Create dictionary to hold nodes
    root = Room("0")
    maze = dict()
    maze["0"] = root

    for line in map_data:
        # Break down data input line
        tokens = line.strip().split(",")

        # Get node of current room - this will always exist since parents are visited before branches
        parent = maze[tokens[0]]

        # Create branches from the current room and add them to the dictionary
        for token in tokens[1::]:
            if token != "X":
                new_room = Room(token)
                maze[token] = new_room

                parent.add_branch(new_room)

    # Find the path from Room 0 to Room E
    escape_path = root.search("E")

    # Turn all room numbers except E into integers and sum them
    escape_path = [int(x) for x in escape_path[0:-1]]
    escape_path_sum = sum(escape_path)

    print(escape_path_sum)

if __name__ == "__main__":
    main()
```

### Output

```plaintext
19939
```

### Alternative Solution

This wasn't the solution provided by the challenge author Alice, though I thought it was neat.

We can walk backwards through the csv file until we find "E" as our starting point, then whatever the parent is, we then have that as our new room to find. Keep repeating until we reach room "0".

```python
def read_map():
    with open("escape_datamap.csv", "r") as file:
        return file.readlines()

def find_path_backwards(map_data):
    # Start from room "E"
    current_room = "E"
    total_sum = 0

    # Walk backward through the map data
    for i in range(len(map_data) - 1, -1, -1):
        line = map_data[i].strip()
        tokens = line.split(",")
        parent = tokens[0]
        children = tokens[1:]

        # Check if the current room is a child of this parent
        if current_room in children:
            if current_room != "E":  # Only sum numeric rooms
                total_sum += int(current_room)
            current_room = parent  # Move to the parent room

            # Stop if we reach room "0"
            if current_room == "0":
                break

    return total_sum

def main():
    map_data = read_map()
    result = find_path_backwards(map_data)
    print(result)

if __name__ == "__main__":
    main()
```
