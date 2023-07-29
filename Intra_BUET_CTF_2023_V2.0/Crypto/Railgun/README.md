# Solution

---

---

### Challenge title: Railgun

#### Points: 50

#### Flag:

```
 |  buetsec{M1K0T015L3V3L6ESC4P3RS}
```

#### Author:

> ```
> C0d3Hunt3r
> ```

### Challenge Description

---

One of my anime lover friend send me an encoded message. But I can't crack what it means as I am not a weeb.
As an anime lover can you solve it for me?

Flag format: buetsec{FL4GH3R3}

[Attachment](./Railgun.txt)

### Solution of Railgun

---

#### Skills need to solve this problem

- Google Dorking
- Rail-Fence Cipher

#### Process

---

+ Reading the problem name , I see that a hint was given as **`Railgun`**.
+ So I searched for `Railgun Cipher`, and after some googling I found something called the ```Rail-Fence cipher```.

+ I also went to a decoder for the **`Rail-Fence Cipher Decoder`** and got this (https://www.dcode.fr/rail-fence-cipher)

![solve](./Photos/solve.PNG)

+ Adjusting the text to the flag format, we got our flag which is:

>```
> buetsec{M1K0T015L3V3L6ESC4P3RS}
>```