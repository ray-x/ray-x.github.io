---
layout: post
title: "Whats new in python 3.10"
author: "Ray"
header-style: text
tags:
    - backend
    - python
date: 2023-12-19
---

# Python 3.10

## Structural Pattern Matching, python version of `switch`

``` python
def respond(language):
    match language:
        case "Java" | "Javascript":  # multiple pattern match
            return "Love those braces!"
        case "Python":
            return "I'm a lumberjack and I don't need no braces"
        case _:  #default
            return "I have no clue!"
```

### We could match against one or more literals by using the OR pattern `|`

## Capturing match

``` python
def op(command):
    match command:
        case ["move", ("F" | "B" | "L" |"R") as direction]:
            return symbols[direction]
        case "pick":
            return symbols["pick"]
        case "drop":
            return symvols["drop"]
        case _:
            raise ValueError(f"{command} does not compute!")
```

### It match `"move F"`, `"move B"` `"move L"` `"move R"`

# \*union\* \~\|\~

``` python
s1 = {'a', 'b', 'c'}
s2 = {'c', 'd'}

s1 | s2 #[[{'a', 'b', 'c', 'd'}]]

d1 = {'c': 3, 'a': 1, 'b': 2}
d2 = {'d': 40, 'c': 30}
d1 | d2  # {'c': 3, 'd': 40, 'a': 1, 'b': 2}

```

# assignment expressions `:=`

## it assign value and return the values

``` python
(x:=1+3) # output 4 and x=4
a = (x := 10 + 20)  # same as a=x=30
```

## examples

``` python
even_results = [
    result
    for i in range(10)
    if (result := slow_function(i, i)) % 2 == 0
]
random.seed(0)
def even_random(n):
    cnt = 0
    while (cnt := cnt + 1) <= n:
        if (number := random.randint(0, 10)) % 2 == 0:
            yield number
```

\*
