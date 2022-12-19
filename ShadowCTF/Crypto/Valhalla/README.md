# ShadowCTF Valhalla Write Up

## Details:
Points: 50

Category: Cryptography

## Write up:

The challenge presented me with the following:

![valhalla](./Original_Files/valhalla.png)

So let's see what is inside "File"

![chall](./Original_Files/runes.PNG)

So we have some wired text in front of us. Now, as `"rune"` is mentioned in the description of the challenge let's google search it. I googled "runes" and found the following:

![runes](./Photos/elder-futhark.jpg)

Using the above image to decode I was able to find the flag:

```
odin was here
```

I also found this link which is useful to decode it. (https://www.dcode.fr/elder-futhark)

![solve](./Photos/solve.png)

``` 
  | Flag: ShadowCTF{odin_was_here}
```