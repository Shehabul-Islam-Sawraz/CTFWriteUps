# Solution

---

---

### Challenge title: Hamza face pic

#### Points: 225

#### Flag:

```
 |  buetsec{fil3_h1d1ng_is_4n_ar7}
```

#### Author:

> ```
> C0d3Hunt3r
> ```

### Challenge Description

---

Hamza laughs hardly. But we got a rare picture of his face where he is laughing. Have fun :)

[Smiley Face](./Photos/Smile.jpg)

### Solution of Hamza face pic

---

#### Skills need to solve this problem

- File Signature
- Hexdump

#### Process

---

After downloading the image, the first thing we should do is open it in `hexdump` or a hex editor.

`$ hexdump -C Smile.jpg`

```
0000c740  00 00 00 00 15 00 0c 00  00 00 00 00 00 00 00 40  |...............@|
0000c750  fd 41 00 0d 00 00 5f 5f  4d 41 43 4f 53 58 2f 7a  |.A....__MACOSX/z|
0000c760  69 70 70 69 64 79 2d 64  6f 6f 2f 55 58 08 00 ff  |ippidy-doo/UX...|
0000c770  1e 06 56 ff 1e 06 56 50  4b 01 02 15 03 14 00 00  |..V...VPK.......|
0000c780  00 08 00 06 ab 39 47 5c  30 0f 34 32 00 00 00 78  |.....9G\0.42...x|
0000c790  00 00 00 1f 00 0c 00 00  00 00 00 00 00 00 40 a4  |..............@.|
0000c7a0  81 43 0d 00 00 5f 5f 4d  41 43 4f 53 58 2f 7a 69  |.C...__MACOSX/zi|
0000c7b0  70 70 69 64 79 2d 64 6f  6f 2f 2e 5f 74 65 78 74  |ppidy-doo/._text|
0000c7c0  2e 74 78 74 55 58 08 00  fd 1e 06 56 eb 1d 06 56  |.txtUX.....V...V|
0000c7d0  50 4b 05 06 00 00 00 00  05 00 05 00 97 01 00 00  |PK..............|
0000c7e0  c2 0d 00 00 ff d9                                 |......|
```

It seems that the file end with the JPEG file trailing bits `FF D9`, but we also see suspicious instances of **`zippidy-doo`**. Let's see if there are any other instances of `FF D9`

Modifying our command to grep for `FF d9`, we see that there are actually **two** instances of it. So the file was trying to mislead us!

`$ hexdump -C Smile.jpg | grep 'ff d9'`

```
0000b870  15 5f ee 8a c7 ff d9 50  4b 03 04 0a 00 00 00 00  |._.....PK.......|
0000c7e0  c2 0d 00 00 ff d9                                 |......|
```

In addition, we see the instances of PK right after the JPG file trailer and at the end of the original image, suggesting a zip file. We copy all of the data after the first `ff d9` into a new [file](./zippi.zip), and unzip it. This gives us a folder called [zippidy-doo](./zippidy-doo/), with a file called [text.txt](./zippidy-doo/text.txt) inside.

Opening the file, we see that it consists of a lot of nonsense. But we got our flag by just searching the flag format:

>```
> buetsec{fil3_h1d1ng_is_4n_ar7}
>```