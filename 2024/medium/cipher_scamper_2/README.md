---
challenge: Cipher Scamper [2]
description: Whilst inspecting the janitor's room, you notice that there is a scrunched-up page tossed in the waste bin. Unraveling the paper, you notice a paragraph of text oddly resembling English, but the letters looks jumbled up. From a glance, you notice certain patterns common to ciphers that are present within the encrypted messages. Time is running short and you have been tasked to decrypt the hidden messages. What secrets does it entail? Only one way to find out.\nMessage for this challenge is attached.
flag: ATR{W4LL_0F_R3D_T3XT}
scoring: decay(500,300,10)
value: 500
category: Medium
authors: Stanley Zhong
---

# Cipher Scamper [2]

[Back to Home](../../README.md)

## Points

Medium - 500 points

## Description

Whilst inspecting the janitor's room, you notice that there is a scrunched-up page tossed in the waste bin. Unraveling the paper, you notice a paragraph of text oddly resembling English, but the letters looks jumbled up. From a glance, you notice certain patterns common to ciphers that are present within the encrypted messages. Time is running short and you have been tasked to decrypt the hidden messages. What secrets does it entail? Only one way to find out.

Message for this challenge is attached. 

Message_Cipher2.txt
```plaintext
F/LNA([/]JNK/L@KJ/XJCC#/MZ[/[GN[/HFNA[/X;CCP?IP]<KP[<W[/@A/GF/L]JJA/C@@DJK/CFDJ/@BJ[GFAH/XJA[/G@]]FMCV/X]@AH/NAK/GJ/L@ZCKA([/IFW/F[/@]/@BJ[GFAH!!!
```

## Solution

The message is a XOR cipher. The challenge is also only available once you solve [Cipher Scamper 1](../../easy/cipher_scamper_1/README.md).

The last part of the solution for [Cipher Scamper 1](../../easy/cipher_scamper_1/README.md) hints at how to solve this challenge with `LOGICALLY EXCLUSIVE OR 0f`. This indicates that the message encoded with a XOR cipher and the key is `0f`. If you didn't work out that the key is `0f`, you can still solve this challenge by brute-forcing the key with a tool like [https://www.dcode.fr/xor-cipher](https://www.dcode.fr/xor-cipher).

After decoding, we get:
```
I CAN'T READ CODE WELL, BUT THAT GIANT W4LL_0F_R3D_T3XT ON HIS SCREEN LOOKED LIKE SOMETHING WENT HORRIBLY WRONG AND HE COULDN'T FIX IT OR SOMETHING...
```

We take the `W4LL_0F_R3D_T3XT` and wrap it in `ATR{}` to get the flag `ATR{W4LL_0F_R3D_T3XT}`.