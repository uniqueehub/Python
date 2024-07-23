Python 3.12.4 (tags/v3.12.4:8e8a4ba, Jun  6 2024, 19:30:16) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
a="aaaa"
b="bbbb"
c="ccc"
print(a + b + c)
aaaabbbbccc
>>> A=["aaa","bbb","ccc"]
>>> print(A)
['aaa', 'bbb', 'ccc']
>>> b=['h','i','n']
>>> print(b)
['h', 'i', 'n']
>>> b.append("g")
>>> print(b)
['h', 'i', 'n', 'g']
>>> b.insert(1,"y")
>>> print(b)
['h', 'y', 'i', 'n', 'g']
>>> len(b)
5
>>> items=A+b
>>> print(items)
['aaa', 'bbb', 'ccc', 'h', 'y', 'i', 'n', 'g']
>>> print(items[3])
h
>>> items[0]="nnnn"
>>> print(items)
['nnnn', 'bbb', 'ccc', 'h', 'y', 'i', 'n', 'g']
>>> "nnn" in items
False
>>> "nnnn" in items
True
>>> "zzzz" in items
False
>>> items[0:5]
['nnnn', 'bbb', 'ccc', 'h', 'y']
>>> items[1:5]
['bbb', 'ccc', 'h', 'y']
>>> len(items)
8
>>> items[1:8]
['bbb', 'ccc', 'h', 'y', 'i', 'n', 'g']
>>> print(items)
['nnnn', 'bbb', 'ccc', 'h', 'y', 'i', 'n', 'g']
