# Solution

---

---

### Challenge title: Frequencies

#### Points: 300

#### Flag:

```
 |  buetsec{sorry_for_JuMbling_files}
```

#### Author:

> ```
> C0d3Hunt3r
> ```

### Challenge Description

---

Kevin is very frustrated as someone jumbled his computer files. Can you find out what is this?

Flag format: buetsec{FlAg_HEre}

[Jumbled](./jumbled.txt)

### Solution of Frequencies

---

#### Skills need to solve this problem

- Python

#### Process

---

It turns out that replacing the characters using [letter frequency](https://en.wikipedia.org/wiki/Letter_frequency) isn't enough. But it's a good start. We can already see some common short words being deciphered correctly. By guessing what other words are supposed to be we can then figure out the rest of the cipher. It's not necessary to recover the whole file to get the flag.
The following [script](./solve.py) is enough to decrypt most of ciphertext.

```python
with open("jumbled.txt", "r") as file:
    content = file.read()

chars = {}
for char in content:
    chars[char] = chars.get(char, 0) + 1

subs = {
    "c": " ",
    "1": "e",
    "T": "t",
    "k": "a",
    "\\": "o",
    "\"": "o",
    "|": "n",
    "w": "h",
    "0": "r",
    ":": "i",
    "2": "s",
    "V": "d",
    "S": "l",
    "K": "m",
    "E": "u",
    "7": "w",
    ")": "c",
    "x": "f",
    "u": "y",
    "]": "p",
    "L": "g",
    "C": "p",
    "i": "b",
    "m": "v",
    "G": "x",
    "e": "a",
    "W": "k",
    "/": "z",
    "h": "t",
    "$": "_",
    "R": "M",
    "r": "m",
    "f": "h",
    "-": "x",
    "a": "q",
    "X": "J",
    "v": "'",
    "#": "."
}

result = ""
for char in content:      
    result += subs.get(char, char)

print(result)
```
So, analyzing the output of the python code carefully, we got the message **`sorry_for_JuMbling_files`**

Thus, adjusting the text to the flag format, we got our flag which is:

>```
> buetsec{sorry_for_JuMbling_files}
>```