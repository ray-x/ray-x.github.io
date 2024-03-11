---
layout: post
title: "Python OOP and MetaProgramming"
tags:
  - python
  - generator
  - iterator
  - metaclass
  - metagrogramming
date: 2023-12-19
---

- [Python+Deep+Dive+4.pdf](../assets/Python+Deep+Dive+4_1696669164886_0.pdf)
- Properties
	- In many languages direct access to attributes is highly discouraged Instead the convention is to make the attribute private, and create public getter and setter methods
	- Python property
		- ((65211fdc-5010-4ade-975c-c0cf9b480269))
		- ((65212021-413d-4bcd-a1c1-81a964e79a45))
	- property decorator `@property`
		- ((652120be-a7ed-40a4-9429-a7b7c1d4eb95))
	- ReadOnly Properties
		- ((6521213b-5183-4825-bca2-9dec4e4565c2))
- Class Scope
	- ((652121ac-37ec-428c-90ba-8a4dd4b79ac0))
	- ((652121e6-0bca-48f3-9aae-de800eed9d41))
	-
- Enumerators And Alias
	- Enum class

	  ``` python
	  class Color(Enum):
	    red = 1
	    crimson = 1
	    carmine = 1
	    blue = 2
	    black = 3
	  ```
	- auto values
		- `enum.auto()` generate a auto values for enum
- MetaProgramming
	- `type`
		- `type` is a **class**

		  ``` python
		  class type:
		  	def __init__(self):
		  		在空值初识话数据

		  	def __new__(self):
		          # __new__ from object
		  		创建->创建类
		  ```
			- create a class with `type`: `type(class_name, class_base, class_dict)`
		- `type` allow you create new class programmly
	- Metaclass
		- The class used to create a class, is called **metaclass** of that class, e.g. `MyType` is metaclass of `Person`
		- By dflt, `type` is used to create a new class, but now if `metaclass` specified, it will be replace `type`
		- Create a new class from MyType
		  MyType

		  ``` python
		  class MyType(type):

		      def __new__(cls, *args, **kwargs):
		          xx = super().__new__(cls, *args, **kwargs)
		          return xx
		  ```
			* method 1 use MyType()

		  ``` python
		  Foo = MyType("Foo", (object,), {"v1": 123, "func": lambda self: 999})
		  ```
			* method 2 use metaclass

		  ``` python
		  class Foo(object, metaclass=MyType):
		      v1 = 123
		      def func(self):
		          return 999
		  ```
		- If Base class created with metaclass, all child/grandchild class of Base will be create with same metaclass
		- ((652124f8-b924-4054-8d9b-e56256794d28))
		-
