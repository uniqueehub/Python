Python 3.12.4 (tags/v3.12.4:8e8a4ba, Jun  6 2024, 19:30:16) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a="hi"
>>> b="Nikita"
>>> print(a+b)
hiNikita
>>> b=" Nikita"
>>> print(a+b)
hi Nikita
>>> print(a+" "+b)
hi  Nikita
>>> a="I am learning things fast"
>>> b=45
>>> print(a+b)
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    print(a+b)
TypeError: can only concatenate str (not "int") to str
>>> print(a+str(b))
I am learning things fast45
>>> a="Sanjivani college"
>>> print(a[0:3])
San
>>> print(a[6:15])
ani colle
>>> print(a[8:20])
i college
>>> print(a[:18])
Sanjivani college
>>> print(a[0:])
Sanjivani college
>>> print("hi
...       
SyntaxError: unterminated string literal (detected at line 1)
>>> print('''hi
... its
... me''')
...       
hi
its
me
