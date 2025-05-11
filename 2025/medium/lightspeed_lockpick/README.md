---
challenge: Lightspeed Lockpick
description: "You and your crew notice a simple electronic lock by a sealed door, promising to contain clues about the grand treasure. Thankfully, you have your own key: a small electronic device that will brute force a combination and get you inside. Input the combinations it provides, and break through the layers of security in the lock. Be careful, though, one wrong input and alarms will trip.\n\n*This activity is in-person, in the Staff Halls.*"
flag: ATR{r3d_l1ght_gr33n_l1ght}
scoring: subflags(100, 50, 200)
value: 350
category: Medium
authors: Alice Arvidson
---

# Lightspeed Lockpick

[Back to Home](../../README.md)

## Points

Medium - 350 points

## Description

You and your crew notice a simple electronic lock by a sealed door, promising to contain clues about the grand treasure. Thankfully, you have your own key: a small electronic device that will brute force a combination and get you inside. Input the combinations it provides, and break through the layers of security in the lock. Be careful, though, one wrong input and alarms will trip.

*This activity is in-person, in the Staff Halls.*

## Solution

Teams will play a simple Simon game, being shown a sequence of coloured lights before having to repeat that sequence using associated push buttons. The game will escalate in difficulty, with a longer sequence and shorter time limit. 

- Make sure the Arduino is plugged in and has the code flashed on it, with the hard mode flag set to 0
- Instruct teams that they will be shown a sequence and have to repeat it using the buttons, emphasising that they cannot press the buttons until the sequence is fully shown.
- Press the RESET button on the Arduino to randomise the sequence and start the first round 
- Gameplay
  - A sequence of LEDs will pulse
  - Once the sequence is complete, all LEDs will blink once
  - The push buttons need to then be activated in order to match the sequence, within a time limit
  - Each level has 3 escalating rounds
  - Once the sequence is complete, the LEDs will light up back and forth and the next round will begin
  - Once all rounds are complete, the LEDs will continuously light up back and forth and the game is won
  - If the timer elapses or an incorrect input is given, all LEDs will blink several times and the round is restarted
- Activity facilitator to give out flag once game is complete
- Level 1 can be repeated as many times as needed until completed.
- Level 2 is optional and can be attempted twice. It is completely restarted if teams fail, requiring a manual reset.

### Flags
- Level 1 (3,4,5 lights) - EASY - `ATR{s1m0n_s4yz}` - 50 points
- Level 2 (5,6,7 lights) - MEDIUM - `ATR{r3d_l1ght_gr33n_l1ght}` - 100 points
- Level 2 (7,8,9 lights) - HARD - `ATR{d0nt_bl1nk}` - 200 points
Flag is to be awarded to teams upon successful completion of the respective level. 

Fastest team overall will receive 100 bonus points
