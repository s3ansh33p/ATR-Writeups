---
challenge: Cipher Scamper [1]
description: Whilst inspecting the janitor’s room, you notice that there is a scrunched-up page tossed in the waste bin. Unraveling the paper, you notice a paragraph of text oddly resembling English, but the letters looks jumbled up. From a glance, you notice certain patterns common to ciphers that are present within the encrypted messages. Time is running short and you have been tasked to decrypt the hidden messages. What secrets does it entail? Only one way to find out.\nMessage for this challenge is attached. \n**Message1 is for the subflag. Message_Cipher2_mainflag is for the main flag.**
flag: ATR{MY5T3RI0U5LY_D1S4PP34R3D}
scoring: subflags(200, 100)
value: 300
category: Easy
authors: Stanley Zhong
---

# Cipher Scamper [1]

[Back to Home](../../README.md)

## Points

Easy - 300 points

## Description

Whilst inspecting the janitor’s room, you notice that there is a scrunched-up page tossed in the waste bin. Unraveling the paper, you notice a paragraph of text oddly resembling English, but the letters looks jumbled up. From a glance, you notice certain patterns common to ciphers that are present within the encrypted messages. Time is running short and you have been tasked to decrypt the hidden messages. What secrets does it entail? Only one way to find out.

Message for this challenge is attached. 

**Message1 is for the subflag. Message_Cipher2_mainflag is for the main flag.**

Message_Cipher1.txt
```plaintext
GUNG FPVRAGVFG... GUR JNL UR ZBIRQ QVQA'G YBBX EVTUG GB ZR. ONPX VA GUR FREIRE EBBZ, UR JNF FJ3NG1AT_OH113G5 JURA V YBBXRQ NG UVZ. ARKG=FGNOORQ23GVZRF
```

Message_Cipher2_mainflag.txt
```plaintext
QEFP EXP EXMMBKBA FK QEB MXPQ YBCLOB. F EBXOA ORJLROP QEBOB TXP X DOLRM QEXQ JV5Q3OF0R5IV_A1P4MM34O3A, PFJFIXO QL TEXQ EXP EXMMBKBA KLT. ILDFZXIIV BUZIRPFSB LO 0c
```

## Solution

The first message is encoded in ROT13 which after decoding, we get:
```
THAT SCIENTIST... THE WAY HE MOVED DIDN'T LOOK RIGHT TO ME. BACK IN THE SERVER ROOM, HE WAS SW3AT1NG_BU113T5 WHEN I LOOKED AT HIM. NEXT=STABBED23TIMES
```

We take the `SW3AT1NG_BU113T5` and wrap it in `ATR{}` to get the subflag `ATR{SW3AT1NG_BU113T5}`.

For the second message, it is encoded with a caesar cipher (with key 23). We are hinted at this key with the `NEXT=STABBED23TIMES` at the end of the first message. You could have also brute forced they 26 keys to find the correct one. After decoding, we get:
```
THIS HAS HAPPENED IN THE PAST BEFORE. I HEARD RUMOURS THERE WAS A GROUP THAT MY5T3RI0U5LY_D1S4PP34R3D, SIMILAR TO WHAT HAS HAPPENED NOW. LOGICALLY EXCLUSIVE OR 0f
```

We take the `MY5T3RI0U5LY_D1S4PP34R3D` and wrap it in `ATR{}` to get the main flag `ATR{MY5T3RI0U5LY_D1S4PP34R3D}`.

Note that the last part, `LOGICALLY EXCLUSIVE OR 0f`, will be relevant for [Cipher Scamper 2](../../medium/cipher_scamper_2/README.md)