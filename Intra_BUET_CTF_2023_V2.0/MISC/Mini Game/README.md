# Solution

---

---

### Challenge title: Mini Game

#### Points: 400

#### Flag:

```
 |  buetsec{H4ckItUpH4ckItInL33tM3B3g1n}
```

### Challenge Description

---

Kevin, one of your friend, found a file and notices that the data in the file has been inserted in a mysterious order. Now, you are a forensic engineer at NSA. Can you discover what's behind it?

[Minigame](./minigame.zip)

Note: You will get the flag in format FLG:theflag.

Flag format: buetsec{theflag}

### Solution of Mini Game

---

#### Skills need to solve this problem

- Mathematics

#### Process

---

After extracting the ZIP file provided, we get 2 `.txt` files: `RULES.txt` and a file with weird symbols. The contents of `RULES.txt` are not completely clear but they seem to be some instructions on traversing a path and storing some characters in a `FLAG` string using a stack.

Since `RULES.txt` indicates that the weird characters represent some kind of labyrinth, we can proceed to rename the text file containing them to `maze.txt`. Moving on, we notice that the `$` character is supposed to represent the start of the path. However, there are several of these in our maze. Therefore, we guessed that there were several strings hidden in the maze, and we assumed that one of them would be the flag.

Given the flag format for the CTF, `{FLG:<theflag>}`, we wrote a Python script to find the flag.

[Game Solver](./gamesolve.py)

Adjusting the text to the flag format, we got our final flag which is:

>```
> buetsec{H4ckItUpH4ckItInL33tM3B3g1n}
>```