book={}
book['tom']={
    'name':'tom',
    'address':'1 red street, NY',
    'phone':98989898
}
book['bob']={
    'name':'bob',
    'address':'1 mad heart, NY',
    'phone':36387847
}
import json
s=json.dumps(book)
print(s)
##{"tom": {"name": "tom", "address": "1 red street, NY", "phone": 98989898}, "bob": {"name": "bob", "address": "1 mad heart, NY", "phone": 36387847}}
with open("C:/Code/PycharmProjects/Python/book.txt","w") as f:
    f.write(s)
