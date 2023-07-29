# Solution

---

---

### Challenge title: Lost Treasure

#### Points: 100

#### Flag:

```
 |  buetsec{YOUAREINVITEDTOTHEBUETCSEFEST}
```

#### Author:

> ```
> C0d3Hunt3r
> ```

### Challenge Description

---

Alaric is a fortune seeker. One day he found a treasure box written **`RGLQGSVZGSCMKZTXKGCUDRZOZZXKK`** and a piece of paper. In the paper the following message was written: ***Each successive letter is shifted by  one unit lesser than the preceding one***. Now Alaric can't open the box. Can you help him to find out what's in the trasure box!!

Flag Format: buetsec{FLAGHERE}

### Solution of Lost Treasure

---

#### Skills need to solve this problem

- Python
- Caesar Cipher

#### Process

---

+ As the message in the paper suggests, it is a **Caesar Cipher**

+ So, I wrote a [python code](./solve.py) to automate the shifting. 

+ After running the code, for shifting by value 7, we got the flag *`YOUAREINVITEDTOTHEBUETCSEFEST`*

+ Adjusting the text to the flag format, we got our final flag which is:

>```
> buetsec{YOUAREINVITEDTOTHEBUETCSEFEST}
>```