# Solution

---

### Challenge title: Work! Work!!

#### Points: 25

#### Flag:

```
 |  buet{Never_stop_learning}
```

#### Author:

> ```
> C0d3Hunt3r
> ```

### Challenge Description

---

Can you find the key to success?	

### Solution of Work! Work!!

---

#### Skills need to solve this problem

+ Basic linux commands

#### Process

---

+ Running **`strings`** on the [file](./key2success) provided me with the following:

    ``` 
    strings key2success

    ...
    __gmon_start__
    _ITM_registerTMCloneTable
    u/UH
    buet{NevH
    er_stop_H
    learningH
    []A\A]A^A_
    Constant_learning_is_the_key
    Hey.
    I have a flag for you..
    ```
+ And, I just found something interesting. By looking at the result carefully, I got the flag to be:
  ```
    buet{Never_stop_learning}
  ```