# numbers

3 % 4
3 // 4

pow(math.ceil(3/4)*4, 3)

pow(-1, 1/2)

type(5/3-4/3-1/3)


# strings

x = 'The ant wants what all ants want.'

x.lower()

x.count('ant')

tmp = x.lower()
tmp = tmp.strip(string.punctuation)
tmp.split()

## the object-oriented way -- composition of operations
x.lower().strip(' .').split()
x.lower().strip(string.punctuation).split()

x.replace(' ant', ' chicken')

x[0:4] + x[6:3:-1] + x[7:]

x.replace('ant', 'tna', 1)

# R's %in% operates on entire elements of a character vector

x = 'a' * 5
%timeit len(x)
x = 'a' * 1000000
%timeit len(x)


system.time(nchar(letters))
x = paste0(rep(paste(letters, collapse=''), 100000), collapse='') 
system.time(nchar(x))

# tuples

x = 1; y = 'foo'

z = x,y
a,b = x,y
x = 5; y = 6
y,x = x,y

xy * 5

# lists

x = [1, 3, 5, 7, 9]

x[::-1]

x.reverse()

x.sort()

y = ['b', 'c', 'a']

z = x + y

x.extend(y)


# dictionaries

students = {"Jarrod Millman": [10, 11, 9], 
            "Thomas Kluyver": [11, 9, 10], 
            "Stefan van der Walt": [12, 9, 9]}

students["Yogi Bear"] = [3, 5, 4]
students.update({"Donald Duck": [1, 5, 7]})

students.update(other_students)
students.update(students)

## named lists or vectors (or environments) in R

## R lists are ordered, 'keys' don't have to be unique

# for loops and list comprehension

[1, 2, 3] + 3
## `+` only works to 'add' two like things but here 3 is not a list and Python doesn't add element-wise with recycling (unlike in R) for standard lists

values = [1, 2, 3]
[x + 3 for x in values]

valuesPlus3 = values
valuesPlus3 = [None] * len(values)
for i in range(len(values)):
    valuesPlus3[i] = values[i] + 3

valuesPlus3 = []
for val in values:
    valuesPlus3.append(val + 3)

    
x = zip(['clinton', 'bush', 'obama', 'trump'], ['D', 'R', 'D', 'R'])
for val in x:
    out = type(val)

# functions

def sqrt(x, allowComplex=True):
    if allowComplex or x > 0:
        return(pow(x, 0.5))
    else:
        return(0)


vals = [-1, -2, 5, 0, 3]
[sqrt(val) for val in vals]

def test(x):
    x[1] = 3

y = [0, 1, 2]
test(y)
y

def test(x):
    return(x + y)

y = 7
test(3)

def test(x):
    y = 3
    def test2(w):
        return(w + y)
    return(test2(x))

test(3)
    
# JSON

import json

with open("project/senators-list.json") as infile: 
    data = json.load(infile)

with open("tmp.json", "w") as outfile:
    json.dump(data, outfile, indent=2)

          
