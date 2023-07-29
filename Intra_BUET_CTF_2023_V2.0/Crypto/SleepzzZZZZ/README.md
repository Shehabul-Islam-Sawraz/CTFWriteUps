# Solution

---

---

### Challenge title: SleepzzZZZZ

#### Points: 150

#### Flag:

```
 |  buetsec{damnyoucrackeditfasterthanmekopp}
```

#### Author:

> ```
> C0d3Hunt3r
> ```

### Challenge Description

---

Someone send me the following string, but I have no idea what it actually means!!

**`3505273749470925280525074535364806053848452848260537274507470808`**

The flag will contain small letters(if any).

**Hint:**
+ Do you know what blocks of 2 means?
+ sqrt(qwertyuiopasdfghjklxcvbnm). Oh no!, I can't sleep if people steal my zzZZZs (╥╯﹏╰╥)
+ Use alphabets in their traditional serial while decoding the above string.

### Solution of SleepzzZZZZ

---

#### Skills need to solve this problem

- Block Cipher

#### Process

---

We received this string, but I have no idea what it means! 
`3505273749470925280525074535364806053848452848260537274507470808`

Just by looking at it, it doesn't make that much sense. Let's go for hints.

Focusing on "Blocks of 2" and absence of 'Z' in the final hint, we can say that this has something to do with a sqaure which has one or more letter missing.
After doing a little bit of research, we found out that this problem is related to [Polybius Square](https://en.wikipedia.org/wiki/Polybius_square) but filled with letters from A to Y.

Following the second hint, we divided the string into blocks of two as:

`35 05 27 37 49 47 09 25 28 05 25 07 45 35 36 48 06 05 38 48 45 28 48 26 05 37 27 45 07 47 08 08`

But there is a problem, Polybius Square must have numbers in range of 1 to 5 but given string doesn't fit the criteria.

If we look closely, we can see a pattern. First digit of every 2 bytes block is in range of 0 to 4 and second digit is in range of 5 to 9 (except for digit 5th block from last which is a typo). With this knowledge, we created a Polybius Square as:

|       | **0** | **1** | **2** | **3** | **4** |
| ----- | :---: | :---: | :---: | :---: | :---: |
| **5** |   A   |   B   |   C   |   D   |   E   |
| **6** |   F   |   G   |   H   |   I   |   J   |
| **7** |   K   |   L   |   M   |   N   |   O   |
| **8** |   P   |   Q   |   R   |   S   |   T   |
| **9** |   U   |   V   |   W   |   X   |   Y   |

We translated our string using the above Polybius Square and we got following message:
`35 05 27 37 49 47 09 25 28 05 25 07 45 35 36 48 06 05 38 48 45 28 48 26 05 37 27 45 07 47 08 08`
`D  A  M  N  Y  O  U  C  R  A  C  K  E  D  I  T  F  A  S  T  E  R  T  H  A  N  M  E  K  O  P  P ` = `damnyoucrackeditfasterthanmekopp`

Adjusting the text to the flag format, we got our flag which is:

>```
> buetsec{damnyoucrackeditfasterthanmekopp}
>```