# Solution

---

---

### Challenge title: SubPixel

#### Points: 100

#### Flag:

```
 |  buetsec{PRETTY_PIXEL_MATH}
```

#### Author:

> ```
> C0d3Hunt3r
> ```

### Challenge Description

---

mystery1 - mystery2

[mystery1.png](./mystery1.png)
[mystery2.png](./mystery2.png)

***Hint:*** 
1. Do you know images also support mathematical calculations?

Flag Format: buetsec{FLAG_HERE}

### Solution of SubPixel

---

#### Skills need to solve this problem

- Compose Images
- Image Mathematics

#### Process

---

+ From the hint and problem description, we get the idea that we have to get the *difference* between [image-1](./mystery1.png) and [image-2](./mystery2.png)

+ This problem could be solved in a number of ways. 

```
convert mystery1.png mystery2.png -compose difference -composite -colorspace RGB out.png
```
Or,
```
composite mystery1.png mystery2.png -compose difference out.png  
```
+ This command generates an output [image](./out.png) that contains the difference between the pixels in the two given files. The flag can be then read from the image:

>```
> buetsec{PRETTY_PIXEL_MATH}
>```