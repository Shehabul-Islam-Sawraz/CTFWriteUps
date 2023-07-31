# Solution

---

---

### Challenge title: Hijacked

#### Points: 50

#### Flag:

```
 |  buetsec{c0mp1et3ly_L!nux_m43str0}
```

#### Author:

> ```
> C0d3Hunt3r
> ```

### Challenge Description

---

Someone planted a hidden info on our pictures from Jubilee Motor Rally 2023, but we don't know what it is!
The only clue that we have is that it's owned by a user called `l33t_haxx0r`. Can you find out the hidden info?

[Motor Rally](./Motor%20Rally.zip)

**Hint:**
1. Do you know linux has a tool called exiftool?

### Solution of Hijacked

---

#### Skills need to solve this problem

- Basic Linux
- Exiftool

#### Process

---

The question only gives us the clue that the file is owned by `l33t_haxx0r`. Which, still, is enought to find a file. Linux provides us with a very useful command line utility that can find files based on different attributes, `exiftool`. I only fired up the command, and found the file.
```
exiftool -if '$OwnerName eq "l33t_haxx0r"' -p '$FileName' .
```
The image matching is *`IMG_2443.jpg`*. Open it and got the flag.

![solve](./Photos/IMG_2443.JPG)

>```
> buetsec{c0mp1et3ly_L!nux_m43str0}
>```