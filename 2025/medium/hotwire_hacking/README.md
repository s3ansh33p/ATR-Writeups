---
challenge: Hotwire Hacking
description: "Making your way through the maintenance halls, one of your crew spots an unassuming access hatch. According to your intel, this should lead to further info about the safe. Cracking open a nearby electrical panel, you get to work hotwiring the hatch. Careful, though, security is right around the corner and the panel is set to trip the alarms.\n\n*The team with the fastest time to beat this challenge will receive 100 bonus points*\n\n*This activity is in-person, in the Staff Halls.*"
flag: ATR{w4tch_y0ur_b4ck}
scoring: subflags(100, 50, 200)
value: 350
category: Medium
authors: Alice Arvidson
---

# Hotwire Hacking

[Back to Home](../../README.md)

## Points

Medium - 350 points

## Description

Making your way through the maintenance halls, one of your crew spots an unassuming access hatch. According to your intel, this should lead to further info about the safe. Cracking open a nearby electrical panel, you get to work hotwiring the hatch. Careful, though, security is right around the corner and the panel is set to trip the alarms.

*The team with the fastest time to beat this challenge will receive 100 bonus points*

*This activity is in-person, in the Staff Halls.*

## Solution

Teams have to connect 5 wires in the correct order to bypass a security system and gain access to important information about the safe. The system is alarmed however, and after a certain time limit the alarm will flash and teams will be locked out.

- Make sure both Arduinos are plugged in and have the code flashed on them
- Make sure wires are plugged into digital pins [2, 4, 6, 8, 10] of the Wire Power Arduino (should be board agnostic)
- Instruct teams to connect the wires to analog pins [0, 1, 2, 3, 4] of the Core Logic Arduino
- Press the RESET button on the Core Logic Arduino to randomise the combination and start the timer
- Gameplay
  - Each wire has a certain pin it must be connected to
  - If a wire is connected to the right pin, the corresponding green LED will light up
  - Once all green LEDs are lit, the game is complete
  - If the timer elapses, red LEDs will flash and the game is failed
- Activity facilitator to give out flag once game is complete
- Level 1 can be repeated as many times as needed until completed
- Level 2 and 3 are optional and can be attempted twice and once, respectively.

### Flags
- Level 1 (1m30s) - EASY - `ATR{k1nd4_5u5}` - 50 points
- Level 2 (40s) - EASY - `ATR{w4tch_y0ur_b4ck}` - 100 points
- Level 3 (20s) - MEDIUM - `ATR{sh0rt_c1rcu1t}` - 200 points
Flag is to be awarded to teams upon successful completion of the respective level. 

Fastest team overall will receive 100 bonus points

### Clue for [The Great Treasure Vault](../../narrative/the_great_treasure_vault/README.md)

After successful submission of the main flag, this clue is revealed to the team:

> #1: The total sum of digits in the code is 15.
