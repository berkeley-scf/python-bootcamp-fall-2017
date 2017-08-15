---
title: Introduction to Python
...


Background
================

Etherpad
-----------

We'll use a shared online document hosted at etherpad.net to share code snippets, problem solutions, syntax, etc.

Please open <https://etherpad.net/p/python-bootcamp-fall-2017> in a browser window.

Preparation
---------------

This tutorial assumes you are familiar with R (or possibly another high-level language such as MATLAB). 

You will also need Python and IPython installed on your computer, as well as a few core additional packages, including re, numpy, scipy, matplotlib, and pandas. 

Packages can generally be installed via pip, or via conda if you have the anaconda or miniconda installation of Python.

```{.sourceCode .bash}
## using pip
pip install ipython
pip install numpy
# or to install within your home directory if you do not have admin control of the computer
pip install --user ipython
pip install --user numpy

## using conda
conda list
conda install ipython
```

For additional help with installation, please see the [IPython installation page](http://ipython.org/install.html).


Resources
---------------

Useful written references and tutorials:

-   <https://docs.python.org/2/index.html>
-   <https://docs.python.org/2/library/index.html>
-   <https://scipy-lectures.github.io/>
-   <https://docs.python.org/3/howto/pyporting.html>

Some introductory video lectures:

-   <https://www.youtube.com/watch?v=a_Z_6brm9ZQ>

While working through this tutorial, you should type the example code
snippets at an interactive Python terminal. I recommend using either the
IPython shell or the IPython notebook. To start an IPython shell, type
the following at a bash prompt:

``` {.sourceCode .bash}
ipython
```

To start an IPython notebook, type

``` {.sourceCode .bash}
jupyter notebook
```

Python 2 vs. 3
--------------------------

Python 3 is a new version of Python, which is in some ways incompatible with Python 2. We will use Python 3, though most of the code here will also work in Python 2. 

If you want to write code that works in both, it's a good idea to make use of the *future* package:

``` {.sourceCode .python}
from __future__ import (absolute_import,
                        division,
                        print_function,
                        unicode_literals)
```

 The idea is that by
 using the future package and adding few imports, as above, to the top of your Python
 modules you can write "predominantly standard, idiomatic Python 3 code
 that then runs similarly on Python 2.6/2.7 and Python 3.3+."

Introduction
===============

Formatting Python code
-------------------------

Unlike most languages, in Python indentation determines code blocks, including functions, loops, and if-else statements.

The standard is one tab or 4 spaces, but you can use other spacing if it's consistent within a block of code.

``` {.sourceCode .python}
a = 3
 a = 3  # this will cause an IndentationError, at least in Python itself, if not IPython

if a>=4:    
    print('a is big')
    if(a == 4):
        print('a is 4')
else:
    print('a is small')

if a>=4:    
  print('a is big')
  if(a == 4):
        print('a is 4')
  else:
        print('a is not 4')
```

Objects
-------

Everything is an object in Python. Roughly, this means that it can be
tagged with a variable and passed as an argument to a function. Often it
means that everything has *attributes* and *methods*.

Certain objects in Python are mutable (e.g., lists, dictionaries), while
other objects are immutable (e.g., tuples, strings, sets). Mutable means one can change parts of the object.

Many objects
can be composite (e.g., a list of dictionaries or a dictionary of lists,
tuples, and strings).

``` {.sourceCode .python}
myList = [1, 2, 'foo']
myList[1] = 2.5
myList

myTuple = (1, 2, 'foo')
myTuple[1] = 2.5
myTuple
```

Variables
---------

As in R and other interpreted languages, variables are not their values in Python (think "I am not my name, I am
the person named XXX"). You can think of variables as tags on objects.
In particular, variables can be bound to an object of one type and then
reassigned to an object of another type without error.

``` {.sourceCode .python}
a = 'foo'
a
a * 4
len(a)

a = 3
a
a*4
len(a)
```

Modules, files, packages, import
--------------------------------

While you will often explore things from an interactive Python prompt,
you will save your code in files for reuse as well as to document what
you’ve done. You can use Python code saved in a plain text file from a
Python prompt or other files by importing it. Typically, this is done at
the top of a file (if you are working at a prompt, you just need to
import it before you want to use the functionality).

``` {.sourceCode .bash}
cat test.py  # special IPython functionality to call the operating system
```

``` {.sourceCode .python}
del(a); del(hello)

import test

test.hello()
test.a

hello()
a
```

``` {.sourceCode .python}
from test import *

hello()
a
```


As in R, you can also load in additional supporting packages for extra functionality. 
Here are some examples of importing Python packages:

``` {.sourceCode .python}
import math
from math import cos
import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
```

Style 
-----

Adopting standard coding conventions is good practice.

-   <https://www.python.org/dev/peps/pep-0008/>
-   <https://docs.python.org/2/tutorial/controlflow.html#intermezzo-coding-style>
-   <https://github.com/numpy/numpy/blob/master/doc/HOWTO_DOCUMENT.rst.txt>
-   <http://matplotlib.org/devel/coding_guide.html>

The first link above is the official "Style Guide for Python Code",
usually referred to as PEP8 (PEP is an acronym for Python Enhancement
Proposal). There are a couple of potentially helpful tools for helping
you conform to the standard. The
[pep8](https://pypi.python.org/pypi/pep8) package that provides a
commandline tool to check your code against some of the PEP8 standard
conventions. Similarly,
[autopep8](https://pypi.python.org/pypi/autopep8) provides a tool to
automatically format your code so that it conforms to the PEP8
standards. I have used both a little and they seem to work fairly well.

Documentation and getting help
-------------------------------

The last two links above discuss the NumPy docstring standard. Let’s
briefly see how you might benefit from NumPy docstrings in practice.

``` {.sourceCode .python}
In [1]: import numpy as np

In [2]: np.ndim?
Type:        function
String form: <function ndim at 0x7fcabd864938>
File:        /usr/lib64/python2.7/site-packages/numpy/core/fromnumeric.py
Definition:  np.ndim(a)
Docstring:
Return the number of dimensions of an array.

Parameters
----------
a : array_like
    Input array.  If it is not already an ndarray, a conversion is
    attempted.

Returns
-------
number_of_dimensions : int
    The number of dimensions in `a`.  Scalars are zero-dimensional.

See Also
--------
ndarray.ndim : equivalent method
shape : dimensions of array
ndarray.shape : dimensions of array

Examples
--------
>>> np.ndim([[1,2,3],[4,5,6]])
2
>>> np.ndim(np.array([[1,2,3],[4,5,6]]))
2
>>> np.ndim(1)
0
```

Docstrings are an important part of Python. A docstring is a character string that occurs as the first statement in a module, function, class, or method definition. Such a docstring becomes the __doc__ special attribute of that object. All modules should normally have docstrings, and all functions and classes exported by a module should also have docstrings. 

**Exercises**

-   What happens if you type `np.ndim??` (i.e., use two question marks)?
-   What does `np.ndim()` do? How does it execute under the hood?
    Consider why the following uses of *ndim* both work.
``` {.sourceCode .python}
a = np.array([0, 1, 2])
a.ndim
np.ndim(a)
```
    Now explain why only one of these works.
``` {.sourceCode .python}
a = [0, 1, 2]
a.ndim
np.ndim(a)
```
-   Type `np.ndarray?` at an IPython prompt. Briefly skim the docstring.
    `ndarray` is the basic datastructure provided by NumPy. We will
    examine it in much more detail in the next chapter.
-   Type `np.` followed by the `<Tab>` key at an IPython prompt. Choose
    two or three of the completions and use `?` to view their
    docstrings. In particular, pay attention to the examples provided
    near the end of the docstring and see whether you can figure out how
    you might use this functionality. 


Decoding error messages
--------------------------

Let's run the following code and try to tease out where the error is. The tricky part is that the error occurs within a function where the function comes from a module (separate code file).

``` {.sourceCode .python}
import days

days.print_friday_message()
```

The list of function calls that led to the error is called a *traceback*.  (Note that in R you can get similar output using `traceback()` after an error or setting `options(error = recover)` before an error.)

Data Structures
===============

Python has a number of basic data structure types that are widely used. There are both similarities and differences from basic data structures in R.

-   <https://docs.python.org/2/library/stdtypes.html>
-   <https://docs.python.org/2/tutorial/datastructures.html>
-   <https://docs.python.org/2/reference/datamodel.html>

Numbers
-------

Python has integers, floats, and complex numbers with the usual
operations.

``` {.sourceCode .python}
2*3
2/3

# be careful - if you try `2/3` in Python 2, you'll get different behavior.

x = 1.1
type(x)

x * 2
x ** 2

(type(1), type(1.1), type(1+2j))
y = 1+2j
```


We can apply various functions to numbers, as expected.
``` {.sourceCode .python}
cos(0)

import math
math.cos(0)
math.cos(math.pi)
```

The *math* package in the standard library includes many additional
numerical operations.

``` {.sourceCode .python}
math.
```
```
math.acos       math.degrees    math.fsum       math.pi
math.acosh      math.e          math.gamma      math.pow
math.asin       math.erf        math.hypot      math.radians
math.asinh      math.erfc       math.isinf      math.sin
math.atan       math.exp        math.isnan      math.sinh
math.atan2      math.expm1      math.ldexp      math.sqrt
math.atanh      math.fabs       math.lgamma     math.tan
math.ceil       math.factorial  math.log        math.tanh
math.copysign   math.floor      math.log10      math.trunc
math.cos        math.fmod       math.log1p      
math.cosh       math.frexp      math.modf
```




**Exercises**

- Using the section on "Built-in Types" from the [official "The Python
Standard Library" reference](https://docs.python.org/2/library/index.html), figure out how to compute:
    1.  3 modulo 4,
    2.  $(\lceil \frac{3}{4} \rceil \times 4)^3$, 
    and
    3.  $\sqrt{-1}$.
- Is the result of `5/3 - 4/3 - 1/3` of the integer type? Is the mathematical value seen in Python an integer? Why is this the case?
- Here's a numerical puzzle. Why does the last computation not work, when the others do? And which of these computations don't work in R?
``` {.sourceCode .python}
100000**10
100000.0**10
100000**100
100000.0**100
```

Objects and object-oriented programming
---------------------------------------

We'll talk about this in more detail later, but it's worth mentioning here that Python is an object-oriented language.  What this means is that variables in Python are objects that are instances of a class.

Objects have methods that can be used on them and attributes (member data) that are part of the object. All objects in a class have the same methods and same member data 'slots', but different objects will have different values in those slots.

Note that even the basic numeric structures behave like objects. We can use tab completion to see what methods are available for an object and what member data are part of an object.

``` {.sourceCode .python}
x.
# x.as_integer_ratio  x.hex               x.real
# x.conjugate         x.imag              
# x.fromhex           x.is_integer        
```

Which of those are attributes/metadata ('member data') and which are methods ('member functions')? If it's a method, say `foo`, you can run the method as `x.foo()`. If it's member data, you can see its value with `x.foo`. 

Strings
-------

Strings are immutable sequences of (zero or more) characters.

**Sequences**

Unlike numbers, Python strings are container objects. Specifically, it
is a sequence. Python has several sequence types including strings,
tuples, and lists. Sequence types share some common functionality, which
we can demonstrate with strings.

-   **Indexing** 

    To see how indexing works in Python let’s use the
    string containing the digits 0 through 9.

    ``` {.sourceCode .python}    
    import string
    string.digits 
    string.digits[1]
    string.digits[-1]
    ```

    Note that indexing starts at 0 (unlike R and Fortran, but like C).
    Also negative integers index starting from the end of the sequence.
    You can find the length of a sequence using the *len* function.

-   **Slicing** 
    Slicing allows you to select a subset of a string (or
    any sequence) by specifying start and stop indices as well as a
    step, which you specify using the `start:stop:step` notation inside
    of square braces.

    ``` {.sourceCode .python}
    string.digits[1:5:2]
    string.digits[1::2]
    string.digits[:5:-1]
    string.digits[1:5:-1]
    string.digits[-3:-7:-1]
    ```

-   **Subsequence testing**

    ``` {.sourceCode .python}    
    '23' in string.digits 
    '25' not in string.digits
    ```

**String methods**

``` {.sourceCode .python}
string1 = "my string"
string1.
```
```
string1.capitalize  string1.islower     string1.rpartition
string1.center      string1.isspace     string1.rsplit
string1.count       string1.istitle     string1.rstrip
string1.decode      string1.isupper     string1.split
string1.encode      string1.join        string1.splitlines
string1.endswith    string1.ljust       string1.startswith
string1.expandtabs  string1.lower       string1.strip
string1.find        string1.lstrip      string1.swapcase
string1.format      string1.partition   string1.title
string1.index       string1.replace     string1.translate
string1.isalnum     string1.rfind       string1.upper
string1.isalpha     string1.rindex      string1.zfill
string1.isdigit     string1.rjust       
```

``` {.sourceCode .python}
string1.upper()

string1.upper?

string1 + " is your string."
"*"*10

string1[3:]
string1[3:4] 
string1[4::2]

string1[3:5] = 'ts'
```

``` {.sourceCode .python}
string1 > "ab"
string1 > "zz"
string1.__
```
```
string1.__add__           string1.__len__
string1.__class__         string1.__lt__
string1.__contains__      string1.__mod__
string1.__delattr__       string1.__mul__
string1.__doc__           string1.__ne__
string1.__eq__            string1.__new__
string1.__format__        string1.__reduce__
string1.__ge__            string1.__reduce_ex__
string1.__getattribute__  string1.__repr__
string1.__getitem__       string1.__rmod__
string1.__getnewargs__    string1.__rmul__
string1.__getslice__      string1.__setattr__
string1.__gt__            string1.__sizeof__
string1.__hash__          string1.__str__
string1.__init__          string1.__subclasshook__
```

**Exercises**

- Using this string: `x = 'The ant wants what all ants want.'`, solve the following string manipulation problems using string indexing, slicing, methods, and subsequence testing:
    1.  Convert the string to all lower case letters (don’t change x).
    2.  Count the number of occurrences of the substring `ant`.
    3.  Create a list of the words occurring in `x`. Make sure to remove
    punctuation and convert all words to lowercase.
    4.  Using only string methods on `x`, create the following string:
    `The chicken wants what all chickens want.`
    5.  Using indexing and the `+` operator, create the following string:
    `The tna wants what all ants want.`
    6.  Do the same thing except using a string method instead.
- What can you do with the *in* and *not in* operators?  What R operator is this like and how is it different?
- Figure out what code you could run to figure out if Python is explicitly counting the number of characters when it does `len(x)`?
- Compare the time for computing the length of a (long) string in Python and R. What can you infer about what is happening behind the scenes?


Tuples
------

Tuples are immutable sequences of (zero or more) objects. Functions in
Python often return tuples.

``` {.sourceCode .python}
x = 1; y = 'foo'

xy = (x, y)
type(xy)
xy = x,y
type(xy)

xy
xy[1]

xy[1] = 3
```

**Exercises**

- What's weird about this? What are the types involved?
``` {.sourceCode .python}
z = x,y
a,b = x,y
```
- Create the following: `x=5` and `y=6`. Now swap their values using a single line of code. (How would you do this in R?)
- What happens when you multiply a tuple by a number? how is this different than similar syntax in R?
- What's nice about using immutable objects in your code?

Lists
----

Lists are mutable sequences of (zero or more) objects.

``` {.sourceCode .python}
dice = [1, 2, 3, 4, 5, 6]

dice[1::2]

dice[1::2] = dice[::2]

dice

dice*2

dice+dice[::-1]

1 in dice

dice.extend(dice)
dice2 = dice.copy()
dice.append(dice2)
# if use dice.append(dice) it embeds a pointer to itself 

```

**Exercises**

-  Create a list of numbers. Reverse the order of the items in the list
    using slicing. Now reverse the order of the items using a list
    method. How does using the method differ from slicing? 
- Do you think tuples have a method to reverse the order of its items?
    Why or why not? Check to see if you are correct or not.
-  Using a list method sort your numbers. Create a list of strings and
    sort it. 
- Figure out some different ways of combining your list of numbers with your list of strings to create a single list of mixed type elements.
- Now try to sort the resulting list. What happens?
- What does the following tell you about copying and use of memory in Python?
``` {.sourceCode .python}
a = [1, 3, 5]
b = a
id(a)
id(b)
# this should confirm what you might suspect
a[1] = 5
```

Dictionaries
------------

Dictionaries are mutable, unordered collections of key-value pairs.

``` {.sourceCode .python}
students = {"Jarrod Millman": [10, 11, 9], 
            "Thomas Kluyver": [11, 9, 10], 
            "Stefan van der Walt": [12, 9, 9]}
students
students.keys()
students.values()
students["Jarrod Millman"]
students["Jarrod Millman"][1]
students.
```

**Exercises**

- How can you add an item to a dictionary.
- How do you combine two dictionaries into a single dictionary?
- What are some analogs to dictionaries in R? 
- How are dictionaries different from such analogous structures in R?

Sets
----

Sets are immutable, unordered collections of unique elements.

``` {.sourceCode .python}
x =  {1, 2, 4, 1, 4}
x
x.
```
```
x.add                          x.issubset
x.clear                        x.issuperset
x.copy                         x.pop
x.difference                   x.remove
x.difference_update            x.symmetric_difference
x.discard                      x.symmetric_difference_update
x.intersection                 x.union
x.intersection_update          x.update
x.isdisjoint                   
```

Built-in functions
==================

-   <https://docs.python.org/2/library/functions.html>

Python has several built-in functions (you can find a full list using
the link above). We’ve already used a few (e.g.,
`len(), type(), print()`). Here are a few more that we you will find
useful.

*zip* and *enumerate* create objects that you can iterate through, but you can't view the elements directly except by looping over them. They're useful either to convert to lists or to loop through element by element.

``` {.sourceCode .python}
x = zip([1, 2], ["a", "b"])
list(x)
```

That's sort of like *cbind* in R.

``` {.sourceCode .python}
enumerate(["a", "b"])
list(enumerate(["a", "b"]))
```

We'll soon see an example usage of enumerate within the context of looping.

Some other useful built-in functions are  `abs()`, `all()`, `any()`, `dict()`,
    `dir()`, `id()`, `list()`, and `set()`.

Control flow
============

-   <https://docs.python.org/2/tutorial/controlflow.html>

If-then-else
------------

-   <https://docs.python.org/2/tutorial/controlflow.html#if-statements>

This is as expected. As previously noted, the indentation is important.

``` {.sourceCode .python}
x = 2

if a>=4:    
    print('a is big')
    if(a == 4):
        print('a is 4')
else:
    print('a is small')

if a>=4:    
    print('a is big')
    if(a == 4):
        print('a is 4')
    else:
        print('a is not 4')
```

For-loops (and list comprehension)
----------------------------------

-   <https://docs.python.org/2/tutorial/controlflow.html#for-statements>
-   <https://docs.python.org/2/whatsnew/2.0.html#list-comprehensions>

Here's basic use of a for loop. Once again indentation is critical, in this case for indicating where the loop ends.

``` {.sourceCode .python}
for x in [1,2,3,4]:
    print(x)

for x in [1,2,3,4]:
    y = x*2
    print(y, end=" ")

for x in [1,2,3,4]:
    y = x*2
print(y, end=" ")
```

Building up a list piece-by-piece is a common task, which can easily be
done in a for-loop. List comprehension provides a compact syntax to
handle this task.

``` {.sourceCode .python}
[x for x in range(4)]

y = [-4, 3, -1, 2.5, 7]
[x for x in y if x > 0]  # list comprehension

import string
letters = string.ascii_lowercase

# concise but terse:
[l[1] for l in enumerate(letters) if l[0] > 13]
# better style:
[letter for index, letter in enumerate(letters) if index > 13]

x = zip(['clinton', 'bush', 'obama', 'trump'], ['D', 'R', 'D', 'R'])
for pres,party in x:
    print(pres, party)

# note if we try to do the loop again, we get nothing, because
# we have emptied the iterator when we loop through it
for pres,party in x:
    print(pres, party)
```


**Exercises**

- See what `[1, 2, 3] + 3` returns. Try to explain what happened and why.
- Use list comprehension to perform element-wise addition of a scalar to a list of scalars.
- How would you do the same task using a for loop? The `range` function may be helpful as might the `enumerate` function.
- Use a for loop to iterate through the elements of a zip object and determine the type of the individual elements. 


Functions
===============

-   <https://docs.python.org/2/tutorial/controlflow.html#defining-functions>

Here's an example that illustrates both positional arguments (always first) and named arguments.

``` {.sourceCode .python}
def add(x, y=1, absol=False):
    if absol:
        return(abs(x+y))
    else:
        return(x+y)

add(3)
add(3, 5)

add(3, absol=True, y=-5)

add(y=-5, x=3)
add(y=-5, 3)
```

**Exercises**

- Define a function that will take the sqrt of a number and will (if requested by the user) set the square root of a negative number to 0.
- Now use the function in a list comprehension to operate on a list of numbers.
- What happens if you modify a list within a function in Python; why do you think this is?
- What happens if you modify a single number (scalar) within a function in Python; why do you think this is?
- Recall how scoping works in R in terms of where objects are looked for if not found locally in a function (i.e., lexical scoping). Empirically assess how scoping works in Python.



Data formats
============

CSV
---

-   <https://docs.python.org/2/library/csv.html>

The Python standard library provides a package for reading and writing
CSV files. This is a somewhat low-level library, so in practice you will
often use NumPy, SciPy, or Pandas CSV functionality.

JSON
----

-   <https://docs.python.org/2/library/json.html>

However the JSON package in the standard library is much more useful.

``` {.sourceCode .python}
import json

x = {"name": "Jarrod", "department": "Biostatistics"}

with open("tmp.json", "w") as outfile: 
    json.dump(x, outfile)

cat tmp.json  # special IPython functionality

with open("tmp.json") as infile:
    y = json.load(infile)

y
```

Note that `cat` is not a Python statement. IPython is clever enough to
guess that you want it to call out to the underlying operating system.

**Exercise**

-   One of the nice things above the JSON format is that it so well
    structured that it easy for a machine to parse, but simple enough
    that it easy for humans to read. By default `json.dump` writes
    everything out to disk without line breaks. For readability
    purposes, use `json.dump?` to figure out how to pretty-print the
    text as well as sort it alphabetically by key.
-   Read in one of the JSON files in the *project* directory and experiment with pretty-printing it when you dump it back out to a file.

Standard library
================

-   <https://docs.python.org/2/tutorial/stdlib.html>

Python provides a wealth of functionality in its huge standard library.
We’ve already seen several packages in the standard library (e.g., math, csv, json). If you need some
functionality the standard library is one of the first places to look.

Here are a couple packages that you may find useful.

os
--

-   <https://docs.python.org/2/tutorial/stdlib.html#operating-system-interface>

``` {.sourceCode .python}
import os

os.getcwd()
pwd           # IPython operating system call
```

**Exercise**

-   Use `os?` and `dir(os)` to explore the os package.

re
--

-   <https://docs.python.org/2/howto/regex.html>

The `re` package provides support for regular expressions.

Math, statistics, and plotting
======================

Numpy and scipy
-------------

Standard lists in Python are not amenable to mathematical manipulation unlike standard vectors in R. Instead we generally work with numpy arrays. These arrays can be of various dimensions (i.e., vectors, matrices, multi-dimensional arrays).

``` {.sourceCode .python}
z = [0, 1, 2] 

y = np.array(z)
y*3

y.dtype


x = np.array([[1, 2], [3, 4]], dtype=np.float64)
x*x
x.dot(x)
x.T

np.linalg.svd(x)

e = np.linalg.eig(x)

e[0]  # first eigenvalue (not the largest in this case...)
e[1][:, 0] # corresponding eigenvector
```

All of the elements of the array must be of the same type.

There are a variety of numpy functions that allow us to do standard mathematical/statistical manipulations. 

Here we'll use some of those functions in addition to some syntax for subsetting and vectorized calculations.

``` {.sourceCode .python}
np.linspace(0, 1, 5)

np.random.seed(0)
x = np.random.normal(size=10)

pos = x > 0

y = x[pos]

x[[1, 3, 4]]

x[pos] = 0

np.cos(x)
```

scipy has even more numerical routines, including working with distributions and additional linear algebra.

``` {.sourceCode .python}
import scipy.stats as st
st.norm.cdf(1.96, 0, 1)
st.norm.cdf(1.96, 0.5, 2)
st.norm(0.5, 2).cdf(1.96)
```

**Exercise**

- See what happens if you try to create a 2-d numpy array with one column of numbers and one column of characters/strings.
- Try to add a vector to a matrix; how does this compare to R?
- How do you compute the variance of each column of a matrix (akin to `apply(x, 2, var)` in R)?


Pandas
---------

Pandas provides a Python implementation of R's dataframe capabilities. Let's see some example code.

``` {.sourceCode .python}
import pandas as pd
dat = pd.read_csv('gapminder.csv')
dat.head()

dat.columns
dat['year']
dat.year
dat[0:5]

dat.sort_values(['year', 'country'])

dat.loc[0:5, ['year', 'country']]  # R-style indexing

dat[dat.year == 1952]

ndat = dat[['pop','lifeExp','gdpPercap']]
ndat.apply(lambda col: col.max() - col.min())
```

Now let's see the sort of split-apply-combine functionality that is popular in dplyr and related R packages.

``` {.sourceCode .python}
dat2007 = dat[dat.year == 2007].copy()  # .copy() ensures a (shallow) copy is made

dat2007.groupby('continent', as_index=False).mean()

def stdize(vals):
    return((vals - vals.mean()) / vals.std())

dat2007['lifeExpZ'] = dat2007.groupby('continent')['lifeExp'].transform(stdize)
```

**Exercise**

- Use *pd.merge()* to merge the continent means for life expectancy for 2007 back into the original *dat2007* dataFrame.
- Explore the pandas documentation to see if  there is a way to add the continent means as a column without an explicit merge (i.e., mimicing capability built into dplyr)?

Matplotlib
---------------

Work through the material in [the Matplotlib tutorial](http://matplotlib.org/users/pyplot_tutorial.html) and then solve the following problems.


**Exercise**

- Make a scatterplot of lifeExp vs gdpPerCap for 2007; make sure you have nice axis labels and title.
- Consider whether plotting income on a logarithmic axis is a better way to display the data.
- Now make an array of plots (in one figure) where each subplot is a different year.
- Now modify the plot so that the color of the point indicates the continent and add a legend that explains this (hint: it's probably easier to do this with plt.scatter than plt.plot). Hint: This snippet of code can help with relating continents to particular colors: `dict(zip(conts, colors))`.
- Find an outlier whose lifeExp is unexpectedly high or low and add text in the plot that associates the point with the name of the country (e.g., I suspect Cuba will be unexpectedly high and an oil-producing country may be unexpectedly low).

Classes
=======

-   <https://docs.python.org/2/tutorial/classes.html>

We've already seen a bunch of object-oriented behavior. Here we'll see how to make our own classes and objects that are instances (realizations) of a class.

``` {.sourceCode .python}
class Rectangle(object):
    dim = 2  # class variable
    counter = 0
    def __init__(self, height, width):
        self.height = height  # instance variable
        self.width = width    # instance variable
        self.set_diagonal()
        Rectangle.counter += 1
    def __repr__(self):
        return("{0} by {1}".format(self.height, self.width))        
    def area(self):
        return(self.height*self.width)
    def set_diagonal(self):
        self.diagonal = pow(self.height**2 + self.width**2, 0.5)

x = Rectangle(10, 5)

x.dim
x.dim = 'foo'
x.dim # hmmm

x.area()
Rectangle.area(x)

y = Rectangle(4, 8)
y.counter
x.counter
```


Mini-project
==============

Please open *project.html* and work through the analysis of the Senatorial tweets with your group.

A Note on the Contents
==============

This content was adapted by Chris Paciorek from [material prepared by K. Jarrod Millman](http://www.jarrodmillman.com/capstone/bootcamp/standard.html) and is licensed under the [CC BY-NC-SA 4.0 license](http://creativecommons.org/licenses/by-nc-sa/4.0/).
