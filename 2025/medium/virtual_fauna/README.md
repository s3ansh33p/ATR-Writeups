---
challenge: Virtual Fauna
description: "Part of the Terrestrial History exhibit, holograms of various species from the planet Earth are displayed around for curious patrons. Looking closely, one of your curious crew notices what appears to be writing. Analyse each animal, and piece together the secrets the fauna are hiding to learn more about the museum."
flag: ATR{th3s3_animals_4re_CheekY}
scoring: subflags(150, 300)
value: 450
category: Medium
authors: Raphael Ho
---

# Virtual Fauna

[Back to Home](../../README.md)

## Points

Medium - 450 points

## Description

Part of the Terrestrial History exhibit, holograms of various species from the planet Earth are displayed around for curious patrons. Looking closely, one of your curious crew notices what appears to be writing. Analyse each animal, and piece together the secrets the fauna are hiding to learn more about the museum.

## Solution

Several 3D models of animals have had messages hidden within them, which are pieced together to give a flag. Teams are encouraged to research the file types to figure out how to open them, and to look at these models in a 3D viewer to find the hidden messages.

The flags are hidden inside the animal files, with four animals being a turtle, fish, bunny and monkey
- The first part of the flag should be the `bunny.obj`, which has half of a flag on the bottom of the bunny
- The second part of the flag is in the `monkey.stl`, which has the other half of the flag inside the monkey
- The fish is red herring, and the "flag” is hidden in the obj file as a comment #
- The turtle is hiding a flag on its face, but there are lots of turtles, the flag is just on one of the turtles
  - The flag is on the wrong turtle, so if you unview a certain turtle, it reveals the flag

### Flags
- Fish.obj `ATR{}` - This is a red herring
- `ATR{th3s3_animals_4re_CheekY}` - 150 points
  - Bunny.obj `ATR{th3s3_animals_`
  - Monkey.stl `4re_CheekY}`
- `ATR{i_Lik3_turtl3s}` - 300 points
  - Turtles.fbx

### Clue for [The Great Treasure Vault](../../narrative/the_great_treasure_vault/README.md)

After successful submission of the main flag, this clue is revealed to the team:

> #9: 6 is the fourth digit in sequence.
