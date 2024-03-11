---
layout: post
title: "Docker storage"
tags:
  - python
  - generator
  - iterator
date: 2023-12-19
---

- [Python+Deep+Dive+2.pdf](../assets/Python+Deep+Dive+2_1696586942514_0.pdf)
- List Comprehension
	- nested

	  ``` python
	  [(i, j) for i in range(1, 6) if i%2==0 for j in range(1, 6) if j%3==0]
	  [[i*j for j in range(5)] for i in range 5]
	  ```
- Generator
	- something that `yield` is a generator
	- List comprehension build with `[]`, generator expression build with `()`
		- `(i**2 for i in range(5))`
		- **Lazy** evaluation and local scope . get value of `i**2` until `next`
	- `yield` and `yield from` (python 3.3)
		- `yield` is used to produce a value from the generator and to suspend the function's state so that it can be resumed right from where it left off.
		- It essentially allows the function to return a value (like a regular function would with `return`) but remembers its state for future calls.

		  ``` python
		  def simple_generator():
		      yield 1
		      yield 2
		      yield 3

		  gen = simple_generator()

		  print(next(gen))  # Output: 1
		  print(next(gen))  # Output: 2
		  print(next(gen))  # Output: 3
		  ```
		- `yield from` is used to delegate part of its operations to another generator. This simplifies the code when a generator function is calling another generator function. It's a way to yield all values from another iterable (often another generator) without using a loop.
		- Example:

		  ``` python
		  def generator_without_yield_from():
		      for item in simple_generator():
		          yield item

		  gen = generator_without_yield_from()

		  print(next(gen))  # Output: 1
		  print(next(gen))  # Output: 2
		  print(next(gen))  # Output: 3

		  # with yield from
		  def generator_with_yield_from():
		      yield from simple_generator()

		  gen = generator_with_yield_from()

		  print(next(gen))  # Output: 1
		  print(next(gen))  # Output: 2
		  print(next(gen))  # Output: 3
		  ```
		- User case
			- `yield`: When you're producing values in a generator function.
			- `yield from`: When you want to delegate yielding values to another generator (or any iterable) within a generator function.
			- also `yield from` is useful when `with open(filename) as f:` context and you should `yield from` instead of `yield` or `return` the lazy iterator inside context
- Set
	- operations
		- `|` : union, `set1|set2|set3`
		- `&`: join `set1 & set2 & set3`
		- `-`: difference  `set1 - set2`
		- `^`: semmetric difference,  same as `(s1 | s2)  -( s1 & s2 )`
		- `<` and `<=` **containment**,  `>` and `>=`
	- mutate a set
		- `|=`, `&=`, `-=`, `^=`
		-
	- frozenset is a const set
	-
