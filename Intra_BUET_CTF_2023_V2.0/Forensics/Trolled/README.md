# Solution

---

---

### Challenge title: Trolled

#### Points: 100

#### Flag:

```
 |  buetsec{fil3_s!gn4tur3_troll3d}
```

#### Author:

> ```
> C0d3Hunt3r
> ```

### Challenge Description

---

Recently I got attacked by a ransomware and the attacker claims that he has a secret picture of me. But I can't open it and I haver already paid him $496 to check it. Can you help me to open the file??

[trolled](./trolled)

### Solution of Trolled

---

#### Skills need to solve this problem

- File Signature
- Hexdump

#### Process

---

Using hexdump (or opening up the file in a hex editor), we notice suspicious instances of PK, which is common to zip files.

`$ hexdump -C trolled`

```
00000000  50 4b 03 04 14 00 00 00  08 00 42 83 d8 56 6a 3e  |PK........B..Vj>|
00000010  1d 55 b9 57 0a 00 3c 63  0a 00 08 00 00 00 6c 69  |.U.W..<c......li|
00000020  61 72 2e 70 6e 67 cc fd  75 54 1c d1 d7 36 88 42  |ar.png..uT...6.B|
00000030  08 90 e0 84 e0 34 ee ee  ee ee 24 b8 4b 70 77 87  |.....4....$.Kpw.|
00000040  86 e0 04 77 77 77 77 77  6b 5c 1b 77 77 77 6e f2  |...wwwwwk\.wwwn.|
00000050  7b df 6f be f9 e6 ce bd  7f dc 99 59 eb d6 ea ea  |{.o........Y....|
```
So, I changed the filename from `trolled` to `trolled.zip`. Unzipping the file, we get a new file with a `.png` extension. Unfortunately, the file seems broken. Opening it up in hexdump again, we notice `IHDR` at the beginning of the file and `IEND` at the end, indicating that it is indeed a PNG file.

`$ hexdump -C liar.png`

```
00000000  0d 0a 1a 0a 0d 0a 1a 0a  00 00 00 0d 49 48 44 52  |............IHDR|
00000010  00 00 03 76 00 00 03 b2  08 06 00 00 00 3f d4 47  |...v.........?.G|
```

```
000a6320  b1 bc 2b 28 28 90 ff 0f  db e1 6e a3 3f 71 71 f7  |..+((.....n.?qq.|
000a6330  00 00 00 00 49 45 4e 44  ae 42 60 82              |....IEND.B`.|
```

However, a quick look at the [wikipedia](https://en.wikipedia.org/wiki/Portable_Network_Graphics) page tells us that the file is lacking important information in the header, namely the first 4 bytes of the file signature.

In a hex editor, we prepend the bits `89 50 4e 47` to the very beginning of the file, save it, and reopen the image. This gives us the flag.

![](./Photos/solve.png)

So, we got our flag:

>```
> buetsec{fil3_s!gn4tur3_troll3d}
>```