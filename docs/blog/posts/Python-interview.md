---
layout: post
title: "Python Fundamental"
author: "Ray"
header-style: text
tags:
    - backend
    - python
date: 2023-12-19
---

<details>
  <summary><h2>string.strip()</h2></summary>
  
  ### Usage
  1. remove all empty
  2. it allows arguments e.g. \'abbabbacdef\'.strip(\'ab\'). it remove both `a` and `b` (the sequence does not matter)

  ### exampls
  ```python
  string.strip("   aaa \n ")
  ```
</details>


<details>
  <summary><h2>calculate total of 1\~100 #card</h2></summary>
  
  ### Usage
    1. sum and range
  ### exampls
  ```python
  sum(range(1, 100))
  ```
</details>


## sum(range(1, 100))

# remove \'key\' from dict #card

## del dict\[\'key\'\]

# merge two dict， dict1 and dict2 #card

## dict1.update(dict2)

# deduplicate from a list #card

## use set

`list(set(mylist))` \*\*

# `*args` and `**kwargs` #card

## args: positional arguments

## kwargs: kv arguments (dict)

# What is dectorator #card

## a function return function and the argument is a function

# difference between `__init__` and `__new__` #card

## `__init__` 是初始化方法，创建对象后，就立刻被默认调用了，可接收参数, first arg is `self`

## `__new__` take `cls` which is current class. It need to return the new class

# `with` #card

## it implement `finally: file.close()`

# \[1,2,3,4,5\] -\> \[1,4,9,16,25\] #card

## list comprehension: \[i\*i for i in l\]

## map: map(lambda x: x\*x, \[1,2,3,4,5\])

# s=\'abccba\' deduplicate and sort #card

## `''.join(sorted(list(set(s)))`

# What is difference between `remove` , `discard`, `del` and `pop` when remove a element from a list #card

## `remove(v)` remove first element with value v

## del l\[2\] remove element from l at pos 2

## pop(idx=-1)

## discard does not raise exception when key not existed

# Sort a dict based on key #card

## `sorted(dict.items(),  key=lambda i: i[0], reverse=False)`

# find all odd number in a list #card

## list comprehension \[i for i in l if i%2==1\]

## filter(): filter(lambda i i%2==1, \[1,2,3,4\])

# merge two list l1, l2 and sort #card

## `l1.extend(l2); sorted(l1)`

# `a=[[1, 2], [3, 4]]` -\> \[1,2,3,4\] #card

## two steps `[ j for i in a for j in i  ]` \~for i in a \~ each i is \[1, 2\], \[3, 4\]; for j in i -\> 1,2 3, 4

\*\*
