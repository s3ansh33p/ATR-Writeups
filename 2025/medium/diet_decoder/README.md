---
challenge: Diet Decoder
description: "You're in the bustling cafeteria of the space museum, surrounded by a variety of space ration packs. You’re not here to eat but you are here to steal. As you walk in, you see 7 foods displayed in glass cases. A inscription reads:\n\n\"Are you hungry or you greedy? Identify the snack with these conditions to find out…\nOver 90 calories\nAt least 18g protein\nLess than 40mg sodium\"\n\n*This activity is in-person, in the Cafeteria.*"
flag: (ATR{)?[r][4a]ph[_ ]b[4a]r[5s](})?
scoring: standard(200)
value: 200
category: Medium
authors: Justis Koh
---

# Diet Decoder

[Back to Home](../../README.md)

## Points

Medium - 200 points

## Description

You're in the bustling cafeteria of the space museum, surrounded by a variety of space ration packs. You’re not here to eat but you are here to steal. As you walk in, you see 7 foods displayed in glass cases.

An inscription reads:

“Are you hungry or you greedy? Identify the snack with these conditions to find out…
- Over 90 calories
- At least 18g protein
- Less than 40mg sodium"

*This activity is in-person, in the Cafeteria.*

## Solution

Each of the labels have Calories, Protein and Sodium values in binary. Participants were required to convert the binary values to decimal and check if they met the conditions.

| Food Item         | Calories (Binary) | Protein (Binary) | Sodium (Binary) |
|-------------------|-------------------|------------------|-----------------|
| Astro-Mie         | 01001000 (72)     | 00010100 (20)    | 00100110 (38)   |
| Tam Tims          | 01000011 (67)     | 00001111 (15)    | 00101000 (40)   |
| Raph Bars         | 01011100 (92)     | 00010010 (18)    | 00100100 (36)   |
| Koka Koala        | 01010101 (85)     | 00010111 (23)    | 00100011 (35)   |
| Cutter Bhicken    | 01010101 (85)     | 00010111 (23)    | 00100011 (35)   |
| Nova Berry Jam    | 01100100 (100)    | 00011000 (24)    | 00110001 (49)   |
| LeBiscuits        | 01010010 (82)     | 00010000 (16)    | 00100110 (38)   |

The only food item that met all the conditions was **Raph Bars**. The flag was therefore `ATR{RAPH_BARS}`.
