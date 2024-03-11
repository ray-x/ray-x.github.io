---
layout: post
title: "python basic"
institute: udemy
language: python
type: programming
instructor: Dr. Fred Baptiste https://www.udemy.com/user/fredbaptiste/
tags:
  - fp
  - decorator
desc: decorator is a design pattern that allows you to modify the functionality of a function by wrapping it in another function.
url: https://docs.python.org/3/library/operator.html#module-operator
id: 65100808-8929-4581-a57b-c1f9470e4eb6
date: 2023-12-19
---

- [Python+Deep+Dive+1.pdf](../assets/Python+Deep+Dive+1_1694868717879_0.pdf)
- Refresher
	- Multi-line Statement in Python:
		- To extend the statement to one or more lines we can use braces {}, parentheses (), square [], semi-colon “;”, and continuation character slash “\”.
		- For string you can use `'''` or `"""` for a multiple line string
		  ``` python
		  list = [5,
		          4, 3, 2, 1
		          ]
		  print('Initializing a list using the\
		   Implicit multi-line statement', list)
		  g = """geeks
		  for
		  geeks"""
		  # Initializing a mathematical expression
		  # using the Implicit multi-line statement.
		  add = (50 +
		         40 -
		         52)
		  if a \
		    and b:
		    pass
		  ```
	- Variable Naming
		- ((6505ac52-5d0c-4272-8c97-ea3ab05e7dcd))
	- Condition Expression
		- `5 < a < 7` vs `5<a and a<7`
		- ternary
			- `b = 1 if a < 5 else 2`
			- `var = exp1 if con-exp2 else exp2`
	- Continue, break, while, else, try, catch, finally
		- The `continue` statement skips the current iteration of a loop and continues with the next iteration.
		- `finally` will be executed even with `continue|break`
		- loop altogether, and the program continues after the loop. aka `goto loop_exit`
		- Inside try-except-finally

		  ``` python
		  # in a for Statement
		  for x in range(2):
		    try:
		        print('trying...')
		        continue   #break
		        print('still trying...')
		    except:
		        print('Something went wrong.')
		    finally:
		        print('Done!')
		  print('Loop ended.')
		  # Prints trying...
		  # Prints Done!
		  # Prints trying...
		  # Prints Done!
		  # Prints Loop ended.
		  ```
		- finally clause is executed before starting(break; exit) the next iteration.
		- `break` with `for/while-else`
			- If the loop terminates **prematurely** with `break`, the else clause won’t be executed.

			  ``` python
			  # Break the for loop at 'blue'
			  colors = ['red', 'green', 'blue', 'yellow']
			  for x in colors:
			      if x == 'blue':
			          break
			      print(x)
			  else:
			      print('Done!') #will never executed
			  # Prints red green
			  ```
- Variable
	- *Everything* is object
		- e.g. int is <Class 'int'>
	- Python Garbage Collection
		- Viewing reference counts in Python

		  ``` python
		  >>> import sys
		  >>> a = 'my-string'
		  >>> sys.getrefcount(a)
		  >>> del a  # set ref count to 0
		  >>> import gc
		  >>> gc.get_count()
		  (595, 2, 1)
		  >>> gc.collect()
		  577
		  >>> gc.get_count()
		  (18, 0, 0)
		  ```
		- Disabling the garbage collector
			- [Dismissing Python Garbage Collection at Instagram | by Instagram Engineering | Instagram Engineering](https://instagram-engineering.com/dismissing-python-garbage-collection-at-instagram-4dca40b29172)
			- When share memory or object reused repeatedly disable GC can save
		- Python object id() is used to get location of a object
	- Type
		- Python is Dynamic typed, use `type()` to get object type
		- Python access variable data value through reference. Object can bind to different type (change reference) durning execution
	- Mutable vs immutable
		- ((650790fd-e50a-4807-9705-97324dbb967b))
		- Inmutable: create a new object if value changed, `id(my_var)` changes when value changed.
		- Why it is important?
			- Side-effect
			- performance
		- Notes
			- mutable can change id. E.g. `list.appen(val)` vs `list += [val]` vs `list = list+[val]`. The last `list=list+[val]` creates a new object
			- use `append` or `+=` when possible
			- A immutable object can have mutable objects

			  ``` python
			  t = ([1], [3])
			  t[0].append(2)
			  ```
			- immutable are safe from unintended side-effect (e.g. func call)
			- to prevent side-effect, use copy() to shallow copy a mutable object(e.g. list)
	- Share reference
		- python share reference by default
		  ((65079bf5-d1fd-48ef-aa24-680ec28b97cd))
		- With mutable objects e.g. list, Python will **NEVER** create shared reference. This may confusing with

		  ``` python
		  a=[1, 2]
		  b=a #reference
		  c=[1, 2]  #does not share with a/[1,2]
		  ```
		- Python pr-create values [-5, 256] so if value in that range, it will share reference
	- Equality
		- `is` identity operator `id(a) == id(b)`
		- Sample

		  ``` python
		  a = 10
		  b = a
		  a is b
		  a == b
		  a = [1]
		  b = [1]
		  a is not b
		  ```
		- All objects of None are same. Same id and same value `a is None`
	- Numbers
		- Python does handle allication memory/bytes for numbers based on the value, e.g. $2^{1000}$ use 160 bytes
		- The larger the number the more memory
		- `floor` is largest(in stardard number order)

		  ``` python
		  floor(3.3) -> 3
		  floor(-3.3) -> -4
		  ```
			- `/` divide -> float
			- `//` divide floor -> int
			- `%` reminder -> int
			- int(10.9)  -> truncation 10
		- Integer / int
			- constructor  `int(10.1); int(True); int(Decimal("10.2")); int("10")`
			- With Base. `int("1010", 2) ; int("1010", base=2)`
			- `bin() -> "0b1010";  oct() -> "0o12"; hex() -> "0xa"`
			- `sign(x)`: `1 if x >= 0 else -1`
		- Rational and Fraction
			- Franction
				-
				  ``` python
				  From factions import Fraction
				  Fraction(3,4)  #3/4   numerartor, denominator
				  Fraction(3.4)
				  Fraction('3.4')
				  Fraction('3.4') * Fraction(3.4)
				  Fraction(math.sqrt(2)) # will be comn
				  In [17]: y=Fraction(sqrt(2))
				  In [18]: y
				  Out[18]: Fraction(6369051672525773, 4503599627370496)
				  y.limit_denominator(10)
				  ```
				- use y.limit_{ denominator(10)} to round denominator to close to 10
		- Float
			- IEEE 754 double-precision binary float aka binary 64
				- sing 1bit
				- exponent 11bit
				- significant 52 bit
			- Equality
				- `math.isclose(a, b, *, rel​​​​​_​​​​​​​tol=1e - 9, abs​​_​​tol=0.0)`
					- e.g. `math.isclose(3.3, 1+2.3000)`
				- `round(val, digits)`  e.g. `round(3.1415, 2)  -> 3.14`
				- You should always use isclose for compare float
			- Float to int
				- `truncation|math.trunc()`, `floor`, `ceiling`, `rounding`
				- trunc keep the int part. same as `int(val)`
				- `floor` largest integer LE to the val
				- `ceiling`  min{i >= x}
				- round(val, n). closest multiple of 10^{ -n} , n default to 0 so round(val) -> int(val)
					- round(1.25, 1) -> 1.2 (to nearest val with even least significant digit)
					- Banker's Rounding
		- decimal
			- Unlike [floats](https://www.pythontutorial.net/advanced-python/python-float/), Python represents decimal numbers exactly. And the exactness carries over into arithmetic
			- Decimal always associates with a [context](https://www.pythontutorial.net/advanced-python/python-context-managers/) that controls the following aspects:
				- Precision during an arithmetic operation (default 28)
				- Rounding algorithm
			- Sample

			  ``` python
			  import decimal
			  from decimal import Decimal
			  decimal.getcontext().prec = 2
			  pi = Decimal('3.14159')
			  print( pi * radius * radius )
			  pi = Decimal(sign, (d1, d2, d3, ...), exp)
			  pi = Decimal (0, (3, 1, 3, 1, 5), 4)

			  10.0 == Decimal('10.0')  # .0 will be use
			  0.1 != Decimal('0.1') #  print('{:.20f}'.format(0.1)) 0.10000000000000000555
			  ```
			- Decimal arithmetic operators
				- `//` and `%`
				- `Decimal(a)//Decimal(b)` -> `trunc(a/b)`
		- Complex number
			- use `cmath`
	- Boolean
		- Boolean is subclass of `int` but it is used in totally different way. Every object in python has a `truth value` (truthiness)
		- `bool` class
			- `True` and `False`
			- isubclass of int `issubclass(bool, int)`
			- wired truth of bool
			- `isinstance(True, int)`  -> `True`
			- True -> 1; False->0  (int(True)->1; True == 1 ; True > False)
				- True + True = 2
			- They are singleton object
			- You can use both `a==True` and `a is True` because it is singleton
		- Truthy
			- All objects are True except
				- None
				- False
				- classes implement `__bool__` or `__len__` that return `False` or `0`.
				  Default of `__bool__` is `return self != 0`
				  e.g. `bool(100)` will execute `int(100).__bool__()` and therefore return result of `100 != 0`
				- Based on above following is `False`:
					- 0 **in any numeric type** (0, 0.0, 0+0j)
					- empty collections (list, tuple, string, dict set)
			- for [[javascript]] ((650504dd-d2ad-48f6-b26b-b98d6c5e99dd))
			-
		- Logical operation precedence
			- ()
			- compare `>, < == !=`
			- `in` `is`
			- `and`
			- `or`
		- Short-Circuit
			- Be care that when short-circuited, part of the expression may not executed
		- Logic operations
			- X or Y is equal to `X if X else Y`

			  ``` python
			  x = 32
			  y = 7
			  print(x or y)  # 32
			  x = 0
			  y = 'abc'
			  print(x or y) # abc
			  ```
			- `X and Y`   `X if not X else Y`
				-
				  ``` pyhon
				  x = 10
				  y =  x and 20/x  # y = 2

				  z = (s and s[0]) or ''  # if s: return s[0]; else return ''
				  ```
		- Comparison operators
			- chained comparisons
				- In Python, chaining comparison operators is a way to simplify multiple comparison operations by stringing them together using logical operators. This is also known as “chained comparisons” or “chained comparison operators”.
				- `a==b==c`
				- `a<b<c`
				- `a<b>c`
				- `a>b<c`
				- `a<b<c<d`
				-
				  ``` python
				  exp1 = a <= b < c > d is not e is f
				  ```
- Function
	- Argument and parameter
		- Positional and keyword arguments
			- It following C++ rule. If a positional parameter is defined with default value, every positional parameter after it **must** given a default value

			  ``` python
			  def myfun(a, b=100, c=0): # a positional
			    pass
			  myfun(1)
			  myfun(1, 2)
			  myfun(1, 2, 3)
			  ```
		- keyword argument
			-
			  ``` python
			  myfun(a=1, b=2, c=3)
			  my(1, 2, c=3)
			  myfun(1, c=2) #b skipped and will use default value of 100
			  myfun(c=3, a=1, b=2) # it is ok not follow same order
			  myfun(a=1, 2, 3) # ❌not correct, the rest after `a=1` must be named
			  ```
		- Function arguments list is ((650994bb-61c3-4e01-b5a0-e7eeda531610))
			- `*arg` to accept variable length arguments
				- example

				  ``` python
				  def func(a, b, c)
				    pass
				  l = [1, 2, 3]
				  func(*l)  #unpack  l from list to numbers

				  def func2(a, b, *args)
				    print(a, b, args)
				  func2(10, 20, 1, 2, 3)  # 10, 20 (1, 2, 3)

				  def avg((args):
				    return args and xxxxsum(args)/len(args)
				  ```
				- all arguments after `*arg` must be ^^keyword^^ arugments

				  ``` python
				  def func2(a, b, *args, d)
				    print(a, b, args)
				  func(1, 2, 3, 4, d=5)
				  ```
				- ^^*^^ without name `def func(*, d)` means there are no more positional args, you must provides keyword arguments
					- it means you can not pass arguments other than <<keyword argument>>
					- e.g `func(d=32)`
				- ^^/^^ : `def mod(x, y, /)` means x, and y are << position ONLY parameters >>
			- `**kwargs` to unpack dict
				- used to group keywords arguments
				- can be spicified even if positional arguments not been exausted
				- **NO** parameters can come after **kwargs
				- Sample

				  ``` python
				  def func(*, d, **kwargs):
				    print(d, kwargs)
				  func(d=1, a=2, b=3)   # d=1, kwargs = {'a': 2, 'b':3}
				  def func2(*args, **args):
				    print(args, kwargs)
				  func(1, 2, a=10, b=20)  # (1, 2) {a:10, b:20}
				  ```
				- you **can not** do this: func(a, b, **, ***kwargs)
			- Default arguments #pitfall
				- It created once, the value should be treat as const. If you need the argument to be variable, e.g. `datetime.now()` do not use default argument.
					- Solution: ^^default to None^^
				- Another case, if initialize a default parameter with collection (e.g. list, dict). As same reason above, it will freeze a collection object to variable, if the function reused, the collection object will be resused and it may have incorrect values
					- Solution: ^^default to Nono, not empty collection^^
					- sample:

					  ``` python
					  def func(l =[]):
					    l.appen(1)
					    return l

					  print(func())
					  print(func())  # 1, 1
					  ```
					- This can also be used for recursion remember the results #memoization
						- factorial example:

						  ``` python
						  def factorial(n, cache={}):
						    if n<1:
						      return 1
						    elif n in cache:
						      return cache[n]
						    else:
						      k = factorial(n-1)*n
						      cache[n]=n*factorial(n-1)
						      return k
						  ```
	- First-Class Functions
		- High order functions
			- A function take parameter of another function as arguments
		- Docstring PEP 257
			- 🧑‍🏫A **docstring** is a string literal that occurs as the ^^first statement^^ (exclude comments) in a module, function, class, or method definition. Such a docstring becomes the _{ doc _ special} attribute of that object.
			- function docstr stored in function. _ doc _
			- Sample:

			  ``` python
			  def root():
			      """Return the pathname of the KOS root directory."""
			      global _kos_root
			      if _kos_root: return _kos_root
			        ...
			  def function(a, b):
			      """function(a, b) -> list"""

			  def complex(real=0.0, imag=0.0):
			      """Form a complex number.
			      Keyword arguments:
			      real -- the real part (default 0.0)
			      imag -- the imaginary part (default 0.0)
			      """
			  ```
		- Annotations PEP 3107
			- 🧑‍🏫Function annotations are ^^arbitrary python expressions^^ that are associated with various part of functions.
			- Benefit: help string(e.g. with sphinx), compile check
			- it stored in ` __annotations__` in K:V format
			- <<type hints>>
				- type hints is one form of annotations
			- Sample:

			  ``` python
			  def f(a:str = 'a', b: [1,2,3]) ->str:
			    ...
			  def f2(a:str) -> 'a repeated ' + str(max(x,y)) + ' times'
			    ...
			  ```
		- Lambda Expressions
			- Limitations
				- single line expression
				- no assignment
				- no annotations
			- Syntax

			  ``` python
			  lambda arguments : expression

			  lambda s: s[::-1].upper()
			  def appply_func(x, fn):
			    return fn(x)
			  apply_func(2, lambda x: x**)
			  ```
			- Usages
				- use in sorted `key`

				  ``` python
				  sorted(d, key = lambda s : s.upper())
				  # randomisze a string
				  sorted(d, key = lambda x: random.random())
				  ```
		- Introspection
			- `__name__` function name
			- `__defaults__`, `__kwdefaults__` defaults values
			- `__code__` the code objects includes
				- `co_varnames` : parameters
				- `co_argcount`
			- <<inspect>> module
				- isroutine: func or method
				- getsource | getmoudle | getcomments | signature
		- callable
			- a object like (but not *limited to*) <<functions>> and <<methods>>
			- `callable()` check if a object is callable
			- <<Class>> is callable
			- generators, coroutines, asynchronous generators
			- any objects implements `__call__` <<Class>>
		- {{embed(((6506c411-3211-4b0c-9647-637d211344b3)))}}
		- Partial function
			- samples:
				-
				  ``` python
				  from functools import partial

				  # A normal function
				  def f(a, b, c, x):
				  	return 1000*a + 100*b + 10*c + x

				  # A partial function that calls f with
				  # a as 3, b as 1 and c as 4.
				  g = partial(f, 3, 1, 4)

				  # Calling g()
				  print(g(5))
				  # A partial function with b = 1 and c = 2
				  add_part = partial(add, c = 2, b = 1)

				  # Calling partial function
				  print(add_part(3))
				  ```
			- Use
				- Callback signature
				- Integration with other API
		- Operator
			-
			- The most used functions
			-

			  | Method | Signature | Behaves like |
			  |---|---|---|
			  | `abs` | `abs(a)` | `abs(a)` |
			  | `add` | `add(a,b)` | a+b |
			  | `and_` | `and_(a,b)` | a&b |
			  | `concat` | `concat(a,b)` | string: a+b |
			  | `contains` | `contains(a,b)` | *b in a* |
			  | `countOf` | `countOf(a,b)` | `a.count(b)` |
			  | `delitem` | `delitem(a,b)` | `del a[b]` |
			  | `delslice` | `delslice(a,b,c)` | `del/a[b:c]` |
			  | `div` | `div(a,b)` | a/b |
			  | `eq` | `eq(a,b)` | a==b |
			  | `floordiv` | `floordiv(a,b)` | a//b |
			  | `ge` | `ge(a,b)` | a>=b |
			  | `getitem` | `getitem(a,b)` | `a[b]` |
			  | `getslice` | `getslice(a,b,c)` | `a[b:c]` |
			  | `gt` | `gt(a,b)` | a>b |
			  | `indexOf` | `indexOf(a,b)` | `a.index(b)` |
			  | `invert, inv` | `invert(a)`, inv(a) | ~a |
			  | `is` | `is(a,b)` | a is b |
			  | `is_not` | `is_not(a,b)` | *a* is not *b* |
			  | `le` | `le(a,b)` | a<=b |
			  | `lshift` | `lshift(a,b)` | a<<b |
			  | `lt` | `lt(a,b)` | a<b |
			  | `mod` | `mod(a,b)` | a%b |
			  | `mul` | `mul(a,b)` | a*b |
			  | `ne` | `ne(a,b)` | a!=b |
			  | `neg` | `neg(a)` | -a |
			  | `not_` | `not_(a)` | `not a` |
			  | `or_` | `or_(a,b)` | a | b |
			  | `pos` | `pos(a)` | `+a` |
			  | `repeat` | `repeat(a,b)` | a*b |
			  | `rshift` | `rshift(a,b)` | a>>b |
			  | `setitem` | `setitem(a,b,c)` | a[b]=c |
			  | `setslice` | `setslice(a,b,c,d)` | a[b:c]=d |
			  | `sub` | `sub(a,b)` | a-b |
			  | `truediv` | `truediv(a,b)` | a/b # "true" div -> no truncation |
			  | `truth` | `truth(a)` | `not not a, bool(a)` |
			  | `xor_` | `xor(a,b)` | a^{ b} |
			- Most operator as dunder operater as well e..g. `le` `__le__`
				- dunder is used for object compare e.g. a<b , operator used for lambda and place need a function as argument
			- Samples

			  ```
			  reduce(mul, [1,2,3])  # 6
			  ```
			- In-place operator
				- iadd iand iconcat ifloordiv ilshift imod imul imatual ior ipow isub ixor itruediv
			- attrgetter(attr)
				- 返回一个可从操作数中获取 *attr* 的可调用对象。 如果请求了一个以上的属性，则返回一个属性元组。 属性名称还可包含点号。 例如：
					- 在 f = attrgetter('name') 之后，调用 f(b) 将返回 b.name。
					- 在 f = attrgetter('name', 'date') 之后，调用 f(b) 将返回 (b.name, b.date)。
					- 在 f = attrgetter('name.first', 'name.last') 之后，调用 f(b) 将返回 (b.name.first, b.name.last)
			- `__getattr__`
				- If attr not existed in object this function will be called. e.g.  `obj.func_ont_exist` or `getattr(obj, 'not_existed')`
			- `__getattribute__`
				- always triggered when reference a attribute inside a object
			- itemgetter(item|*item)
				- 返回一个使用操作数的 [[https://docs.python.org/zh-cn/3/library/operator.html#operator.__getitem__][]] 方法从操作数中获取 /item/ 的可调用对象。 如果指定了多个条目，则返回一个查找值的元组。
				- sample

				  ``` python
				  itemgetter(1)('ABCDEFG') #B
				  itemgetter(1, 3)('ABCDEFG')  #('B', 'C')
				  ```
			- methodcaller(*name*, /, **args, ***kwargs)
				- 返回一个在操作数上调用 /name/ 方法的可调用对象。 如果给出额外的参数和/或关键字参数，它们也将被传给该方法

				  ``` python
				  def methodcaller(name, /, *args, **kwargs):
				      def caller(obj):
				          return getattr(obj, name)(*args, **kwargs)
				      return caller
				  class MyClass:
				    def test(self, arg):
				      print("test", arg)
				  obj = MyClass()
				  testfun = attrgetter('test')(obj)
				  testfun("aaa")
				  methodcaller('test', 'aaa')(obj)
				  ```
- Closure
	- Abstract
	- Questions, keywords and cues
```org
:questions-keywords-cues:
		  - What do I already know?
		  - Strengths and weaknesses?
		  - When to apply this theory?
		  - How valid are the research methods?
		  - How strong is the evidence?
		  - How logical is the argument?
		  - How does this fit in to other research in the field?
		  - What do I need to find out next?

:END:
```
		- When to apply this?
	-
---
	- abstract & reflect
```org
:main-idea-checkbox:
		  - What is this aims?
		  - What is the their research question?
		  - What is the author arguing?
		  - What is their answer to the question?
		  - What points support their argument?
		  - What are their main reasons?
		  - What evidence have they used to support their argument?
		  - What’s the significance of these facts?
		  - What principle are they based on?
		  - How can I apply them?  How do they fit in with what I already know?
		  - What’s beyond them?
		  - What're supporting details and explanations?

:END:
```
		- Main points
	- 📖 Scope
		- Scopes and namespace
			- ![python variable scopes](https://favtutor.com/resources/images/uploads/mceu_14589579711675226532035.jpg)
			- It is important when a symbol is hide/blocked by another symbol
		- built-in scope
			- `print`, `True`, `False` etc are located in bult-in scope. If a symbol is not in *module* scope or current LEG, search in built-in scope. This is #LEGB
		- Local Scope
			- inside a function. So it also called *function local scope*
		- Enclosing Scope
			- **nonlocal scope**
			- **nonlocal**
				- The `nonlocal` keyword is used in nested functions to declare that a variable refers to a variable in the nearest enclosing scope that is not global. This means if you have a nested function and you want to modify a variable from the outer (enclosing) function, you'd use `nonlocal`. Sometime the *nonlocal* variable also been called **free variable**
				- free variable
				- Use the keyword `nonlocal` to declare that the variable is not local.
				- When nonlocal can be omitted
					- if it is read after write or read only, you can skip `nonlocal` keyword
			- nested function create an outer and inner scope, use **nonlocal** keyword to refer to the outer scope instead of create a new local variable

			  ``` python
			  def outer():
			      string = "Favtutor" # Local Variable
			      def inner():
			          nonlocal string #declaring a non local variable
			          string= "Python Favtutor Classes" # Overwriting value of a variable string
			          print("inner function:", string)
			      inner()
			      print("outer function:", string)

			  outer()
			  ```
		- Global scope
			- A variable created in the main body of the Python code is a **global** variable and belongs to the global scope. aka *module scope* or *file scope*. It spans a **single file** only
			- Global Keyword
				- If you need to create a global variable, but are stuck in the local scope, you can use the `global` keyword.
				- The `global` keyword makes the variable global.

				  ``` python
				  def myfunc():
				    global x  # create a global variable
				    x = 300
				  myfunc()
				  print(x)
				  ```
		- Global and local
			- **The main difference is that Global is used to access and modify global variables from within a function, while nonlocal is used to access and modify variables from the nearest enclosing scope that is not global.**
			- when python encounter a func definition at compile time. It scans for labels/var that have assigned to them **anywhere** in the function. If the label has not been specified as *global* it is a local
			- Var referenced but not assigned  anywhere in the func will not be local and python at runtime look for them in **enclosing** scopes
			- Nonlocal declarations in a local scope do not require the variable to be pre-bound (it declared in outer scope), which is another fundamental distinction between them. These variables must already have been bound in the surrounding namespace(outer function) to avoid syntax errors.
			- While a nonlocal statement allows for the alteration of an enclosing scope variable in the local scope, a global statement allows for the modification of a global variable in the local scope. Nonlocal variables must already exist, although global variables can be declared with brand-new variables.
			- Sample

			  ``` python
			  a = 10
			  def f3():
			    global a
			    a = 100 # this refer to the a at line 1
			  def f4():
			    print(a)  # this refer to a at next line and will throw a runtime error
			    a = 100
			  ```
		- **del** a symbol in current scope
			- e.g

			  ``` python
			  print = lambda n: print(2**n)
			  print(3)
			  del print
			  ```
		- Cell object
			- **Cell** objects are used to implement variables referenced by multiple scopes. For each such variable, a cell object is created to store the value; the local variables of each stack frame that references the value contains a reference to the cells from outer scopes which also use that variable. When the value is accessed, the value contained in the cell is used instead of the cell object itself. This de-referencing of the cell object requires support from the generated byte-code; these are not automatically de-referenced when accessed. Cell objects are not likely to be useful elsewhere.
			- ((650f9ddb-a02a-45cf-9524-8c395f42f66e))
			- Cell is important to understand **free variables** used in closure
	- 📖 Closure
		- When closure created, it put the  **nonlocal** and **global** variable into a dict ((650f9d5c-c95d-41d3-8f60-6d6ada6c32f2))  and closure can be introspect with `__closure__`
		- if there is no ((65100808-8929-4581-a57b-c1f9470e4eb6)) there is no closure
		- Use closure to remember state
			- ((650fb53c-bad9-4c9b-87c7-acc3a3d2a8b8))
			- When counter() created a closure. It include a reference to counter/cell. So each time `fn()` called, count will change
		- Multiple instance of Closures
			- Each time create a new closure, a **new** scope/env/capture will also created.

			  ``` python
			  f1 = counter()
			  f2 = counter()
			  f1() # -> 1
			  f1() # -> 2
			  f2() # -> 1
			  ```
		- Shared scope and share reference/cell
			- Following code

			  ``` python
			  adders = []
			  for n in range(1, 4):
			    adders.append(lambda x: x + n)
			  adders[0](1)  -> 4
			  adders[1](1)  -> 4
			  adders[2](1)  -> 4

			  # vs
			  adders = []
			  for n in range(1, 4):
			    adders.append(lambda x, y=n: x + y)
			  adders[0](1)  -> 2
			  adders[1](1)  -> 3
			  adders[2](1)  -> 4

			  ```
			- The reason n is **3** for each adder closure is:
				- n is a share scope object in for loop
				- it does not recreated each time
				- each adder has a ((650f9d5c-c95d-41d3-8f60-6d6ada6c32f2)) which is reference to `n`
				- It is important to know closure scope value is stored in ((650f9d5c-c95d-41d3-8f60-6d6ada6c32f2)) and store reference, when the value reference pointing to changed, closure value will also change .
				- Python does not evaluate free vars n until adders[i] func is called. And all of then refer to same n(3) when it is called
		- Replace Class with closure
			- In many cases, the only reason we might have a single-method class is to store additional state for the use in method.
			- A request class

			  ``` python
			  import requests
			  class SourceTemplate:
			      def __init__(self, url):
			          self.url = url
			      def load(self, **kwargs):
			          return requests.get(self.url.format_map(kwargs))
			  github = SourceTemplate('https://api.github.com/repositories?since={since}')
			  github.load(since=200).json()
			  ```
			- A  closure implementation

			  ``` python
			  def sourcetemplete(url):
			      def load(**kwargs):
			          return requests.get(url.format_map(kwargs))
			      return load
			  load = sourcetemplete('https://api.github.com/repositories?since={since}')
			  load(since=200).json()
			  ```
	- Recites
```org
:howto-recite:
		  Cover the notetaking column with a sheet of paper.  Then, looking at the questions or cue-words in the question and cue column only, say aloud, in your own words, the answers to the questions, facts, or ideas indicated by the cue-words.

:END:
```
	-
---
	- Summary
		- main points
	-
- Decorator
	- Abstract
		- The outer function is called the decorator, which takes the original function as an argument and returns a modified version of it.
		- So, in the most basic sense, a decorator is a callable that returns a callable.
		- ((65101822-3477-4dbd-bf27-c6d41cb38579))
	- Questions, keywords and cues
```org
:questions-keywords-cues:
		  - What do I already know?
		  - Strengths and weaknesses?
		  - When to apply this theory?
		  - How valid are the research methods?
		  - How strong is the evidence?
		  - How logical is the argument?
		  - How does this fit in to other research in the field?
		  - What do I need to find out next?

:END:
```
		- What is Decorator?
	-
---
	- abstract & reflect
```org
:main-idea-checkbox:
		  - What is this aims?
		  - What is the their research question?
		  - What is the author arguing?
		  - What is their answer to the question?
		  - What points support their argument?
		  - What are their main reasons?
		  - What evidence have they used to support their argument?
		  - What’s the significance of these facts?
		  - What principle are they based on?
		  - How can I apply them?  How do they fit in with what I already know?
		  - What’s beyond them?
		  - What're supporting details and explanations?

:END:
```
		- Main points
	- 📖 Define a decorator
		- Using nested functions

		  ``` python
		  def counter(fn):
		      count = 0
		      def inner(*args, **kwargs):
		          nonlocal count
		          count += 1
		          print('Function {0} was called {1} times'.format(fn.__name__, count))
		          return fn(*args, **kwargs)
		      return inner

		  def add(a, b=0):
		    "return sun of two integers"
		    return a + b
		  add = counter(add)
		  add(1, 2) # Function add was called 1 times 3
		  ```
		- Pythonic way

		  ``` python
		  @counter
		  def mult(a: float, b: float=1, c: float=1) -> float:
		    "mult return products of three number"
		    return a * b * c
		  ```
		- There is a minor problems that mult is no longer mult after wrapped by operator. The `__doc__` and `__name__` changed. That when `@wraps is needed`

		  ``` python
		  def counter(fn):
		      count = 0
		      @wraps(fn)
		      def inner(*args, **kwargs):
		          nonlocal count
		          count += 1
		          print("{0} was called {1} times".format(fn.__name__, count))
		      return inner
		  ```
		  It is same as this:

		  ``` python
		  def counter(fn):
		      count = 0

		      def inner(*args, **kwargs):
		          nonlocal count
		          count += 1
		          print("{0} was called {1} times".format(fn.__name__, count))
		      inner.__name__ = fn.__name__
		      inner.__doc__ = fn.__doc__
		      return inner
		  ```
		  And also this:
		  ``` python
		  def counter(fn):
		      count = 0

		      def inner(*args, **kwargs):
		          nonlocal count
		          count += 1
		          print("{0} was called {1} times".format(fn.__name__, count))
		      inner = wrap(fn)(inner)
		      return inner
		  ```
		-
	- 📖 Decorator with parameters (Decorator factory)
		- **Decorator with parameters** are wrapper around existing decorators. Decorator returns **closure** but **decorator with parameters** returns decorator.
		- A timer decorator with parameters

		  ``` python
		  # name factory is decorator factory which accepts parameters
		  def factory(number):
		  	# name timer is actual decorator
		      def timer(fn):
		          from time import perf_counter

		  		# name inner is closure
		          def inner(*args, **kwargs):
		              total_time = 0
		              for i in range(number):
		                  start_time = perf_counter()
		                  to_execute = fn(*args, **kwargs)
		                  end_time = perf_counter()
		                  execution_time = end_time - start_time
		                  total_time += execution_time
		              average_time = total_time/number
		              print('{0} took {1:.8f}s on an average to execute (tested for {2} times)'.format(fn.__name__, execution_time, number))
		              return to_execute

		          return inner
		      return timer

		  @factory(50)
		  def function_1():
		      for i in range(1000000):
		          pass

		  @factory(5)
		  def function_2():
		      for i in range(10000000):
		          pass

		  function_1()
		  function_2()

		  ```
	- Recites
```org
:howto-recite:
		  Cover the notetaking column with a sheet of paper.  Then, looking at the questions or cue-words in the question and cue column only, say aloud, in your own words, the answers to the questions, facts, or ideas indicated by the cue-words.

:END:
```
	-
---
	- Summary
		- main points
		-
- Tuple
	- #[[wired fact]] tuple is not created with `()` it is with `,`
		- `(1)` is not a tuple, it is a int, a single int of 1
		- `1, ` is a tuple
		- `1, 2, 3` is a tuple
		- `()` is used just to make code looks nicer
		- create a empty tuple using `tuple()`, `()` will do as well
	- Pack and unpack
		- Similar to ((650504dd-7dea-4c1a-9a18-71aa0e1f2200))
		- `a, b, c = 1, 2, 3`; `a, b, c = [1, 2, 3]`; `(a, b, c) = [1, 2, 3]` they works the same way
		- behind the scenes: a, b, c is a `tuple`
		- `a, b, c = 'XYZ'`   `a='X', b='Y', c='Z'`
		- `for e in 12, 10, 'hello'`
		- swap: `a, b = b, a`
		-
		  ``` python
		  d = {'1': 1, '2':2}
		  a, b = d # a can be '1' or '2'

		  ```
		- extended unpack with `*` and `**`
			-
			  ``` python
			  a, *b = [1, 2, 3] # a=1, b = [2, 3]
			  a, *b = 'XYZ' #b=['Y', 'Z']
			  a, *b, c = 'abcd'  # b=['b', 'c']
			  ```
			- unpack can be used other way around

			  ``` python
			  l1=[1, 2]
			  l2=[3, 4]
			  l = [*l1, *l2]  # 1, 2, 3, 4
			  l3 = 'XYZ'
			  [*l1, *l3] # [1, 2, 'X', 'Y', 'Z']
			  ```
			- unpack dict with `**`
				- merge dict

				  ``` python
				  d1={1:1}
				  d2={1:1, 2:2}
				  d3={1:2: 3:3}
				  d = {**d1, **d, **d3}  # duplicated value will be overwrote
				  ```
			- nested unpacking

			  ``` python
			  a, *b, (c, d, e) = [1, 2, 3, 'XYZ'] # b = [2, 3], c = X ...

			  ```
			- Ignore some of fields when unpack

			  ``` python
			  a, *_, c = (1, 2, 3, 4, 5)   # -> c = 5
			  a, *ignore, c = (1, 2, 3, 4, 5)   # -> c = 5
			  ```
	- Named Tuple
		- namedtuple is a **class factory** return a subclass of tuple.  You need a class_{ name} and array of element names to create it. The name can also be a string of space ` ` or `, ` separated words
		  Syntax:

		  ``` python
		  TupleClass = namedtuple(class_name, ['array', 'elements', 'string', 'format'])
		  TupleClass = namedtuple(class_name,  'string of names')
		  # Sample
		  Point = namedtuple('Point', ['x', 'y'])
		  # Now Point is a class
		  p1 = Point(1, 3)
		  print(p1.x, p1.y)
		  p1 = Point(x=1, y=3)
		  ```
		- Name tuple is tuple so it can use all tuple operations

		  ``` python
		  x = Point[0]
		  x = Point[:1]
		  ```
		- Extend a tuple

		  ``` python
		  Point1D = namedtuple('Point1D', ['x'])
		  fields = Point1D._field+('y',)
		  Point1D = namedtuple('Point2D', fields)
		  ```
	- Optimization
		- Object Interning In Python
			- Object interning is a technique used in Python to optimize memory usage and improve performance by reusing immutable objects instead of creating new instances. It is particularly useful for strings, integers and user-defined objects. By interning objects, Python can store only one copy of each distinct object in memory reducing memory consumption and speeding up operations that rely on object comparisons.
			- Syntax:
			  ``` python
			  import sys
			  interned_string = sys.intern(“string_to_intern”)
			  interned_string2 = sys.intern(“string_to_intern”)
			  interned_string is interned_string2 # faster than str cmp
			  ```
			- All identifiers are interned
		- Peephole
			- In Peephole optimization, Python optimizes code either by **pre-calculating** constant expressions or by **membership tests** (converting mutable data structures to immutable data structures.)
			- [Peephole Optimization in Python](https://www.codesansar.com/python-programming/peephole-optimization.htm)
			- Find what is pre-calculation by using
			  `your_obj.__code__.co_consts`
			-
-
-
-
-
