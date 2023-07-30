# Solution

---

---

### Challenge title: XOR is Fun

#### Points: 225

#### Flag:

```
 |  buetsec{s0_mu6h_g0ing_0n_h3r3!!}
```

#### Author:

> ```
> C0d3Hunt3r
> ```

### Challenge Description

---

Let's start with the basic: ```554252434452544c4407685a42015f6850075e5950680759685f04450416164a```

### Solution of XOR is Fun

---

#### Skills need to solve this problem

- Python

#### Process

---

This is an XOR cipher with key length 1. As the challenge title implies, this is easy to crack. All we have to do is unhexlify the ciphertext and then try to XOR that with all possible ASCII characters until we find the key which results in the flag.

```python
import binascii

str1 = binascii.unhexlify(
    '554252434452544c4407685a42015f6850075e5950680759685f04450416164a'
)

for i in range(255):
    str2 = ''
    for c in str1:
        str2 += chr(c ^ i)
    if 'buetsec{' in str2:
        print(str2)
        break
```

>```
> buetsec{s0_mu6h_g0ing_0n_h3r3!!}
>```