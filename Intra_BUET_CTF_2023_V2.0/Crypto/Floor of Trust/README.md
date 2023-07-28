# Solution

---

---

### Challenge title: Floor of Trust

#### Points: 150

#### Flag:

```
 |  buetsec{fl00r_d1vis!0n}
```

#### Author:

> ```
> C0d3Hunt3r
> ```

### Challenge Description

---

Based on our intelligence, it appears that [new_cipher.py](./new_cipher.py) was utilized for message encryption. We had successfully apprehended a spy during their operation. But, our  interrogators were only able to retrieve the ciphertext [new_cipher.txt](./new_cipher.txt) of a message from the spy's phone. Can you help us in deciphering the concealed message?

### Solution of Floor of Trust

---

#### Skills need to solve this problem

- Python

#### Process

---

<!-- + Reading the description carefully, I see that a hint was given as **`False Bill`**.
+ So I searched for `False Bill Cipher`, and found the following: 

![runes](./Photos/image-25.png)

+ I also went to a decoder for the `FALSS BILL CIPHER DECODER` and got this (https://www.dcode.fr/gravity-falls-bill-cipher)

![solve](./Photos/solve.PNG) -->

The function which was used to encrypt a message was:
```python
def encrypt_message(message, key):
    encrypted = []
    for c in message:
        encrypted.append(str(ord(c) // key))
    return ' '.join(encrypted)

message = "<redacted>"
key = 3
encrypted = encrypt_message(message, key)
print(encrypted)
```

Ciphertext:
```27 39 33 34 10 36 32 33 35 10 37 34 10 38 38 39 38 38 15 15 10 32 39 33 38 38 33 33 41 34 36 16 16 38 31 33 16 39 35 38 11 16 36 41```

In the source code above, we can see that floor division was used during encryption of the message. Floor division means the value after '.' or decimal is truncated. For example, both 5.9999 and 5.0001 when floor divided by 3 result to 1.
From this, we can conclude that for each character there are three possible values.

A simple python script called [solve.py](./solve.py) to decipher the ciphertext and find out the possible values was written. The output with our guess on the right hand side:
&nbsp;&nbsp;&nbsp;`Output` &nbsp;&nbsp;&nbsp; `Our guess`
```
Q | R | S         S
u | v | w         u
c | d | e         c
f | g | h         h
▲ | ▼ |           
l | m | n         l
` | a | b         a
c | d | e         c
i | j | k         k
▲ | ▼ |
o | p | q         o
f | g | h         f
▲ | ▼ |
r | s | t         t
r | s | t         r
u | v | w         u
r | s | t         s
r | s | t         t
- | . | /         .
- | . | /         .
▲ | ▼ |
` | a | b         b
u | v | w         u
c | d | e         e
r | s | t         t
r | s | t         s
c | d | e         e
c | d | e         c
{ | | | }         {
f | g | h         f
l | m | n         l
0 | 1 | 2         0
0 | 1 | 2         0
r | s | t         r
] | ^ | _         _
c | d | e         d
0 | 1 | 2         1
u | v | w         v
i | j | k         i
r | s | t         s
! | " | #         !
0 | 1 | 2         0
l | m | n         n
{ | | | }         }
```
So, based on our guess, we got the message **Such lack of trust... buetsec{fl00r_d1vis!0n}**
From the message, we found the flag to be `buetsec{fl00r_d1vis!0n}`