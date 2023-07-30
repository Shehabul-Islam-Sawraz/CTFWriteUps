# Solution

---

---

### Challenge title: A Thousand Pictures

#### Points: 50

#### Flag:

```
 |  buetsec{it_must_b3_pr3tty_h4rd_r34ding_this}
```

#### Author:

> ```
> C0d3Hunt3r
> ```

### Challenge Description

---

There is a `JPEG` picture among the thousand files that worth a thousand words. Can you help me to find what it tells!!!

[Data](./data.zip)

***Hint:*** 
1. Grep is always there for you 

### Solution of A Thousand Pictures

---

#### Skills need to solve this problem

- Basic Linux Commands

#### Process

---

Here, we were provided 1000+ files, each with random name, and with no file extension. Now, as the problem description says, I ran the following command to find the JPEG image;

```zsh
$file * | grep JPEG
UgeVjTlmZjNFvULk: JPEG image data, JFIF standard 1.01, aspect ratio, density 1x1, segment length 16, baseline, precision 8, 266x71, components 3
```

I found the image, however there were no flags in it. I tried reading its content using `cat` and `strings`, and they were of no help. Finally, I decided to download the file given in question, and opened the image. And, there it was.

>```
> buetsec{it_must_b3_pr3tty_h4rd_r34ding_this}
>```