f=open("C:/Code/PycharmProjects/Python/book.txt","r")
s=f.read()
print(s)
import json
book=json.loads(s)
print(book)
print(type(book))
print(book['bob'])
print(book['bob']['phone'])
for i in book:
    print(book[i])
