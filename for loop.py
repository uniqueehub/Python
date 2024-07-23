exp=[678,786,473,3657,475]
print(exp)
total=0
for i in exp:
    total=total+i
print(total)
#output:
#[678, 786, 473, 3657, 475]
#6069
for i in range(1,11):
    print(i)
#output:
#1
#2
#3
#4
#5
#6
#7
#8
#9
#10
for i in range(12,20):
    print(i*i)
#output:
#144
#169
#196
#225
#256
#289
#324
#361
key='dd'
loc=['aa','bb','cc','dd','ere']
for i in loc:
 if (i==key):
    print("key found ",i)
    break
 else:
    print("not found ",i)
#output
#not found  aa
#not found  bb
#not found  cc
#key found  dd
e=[3,5,6,7,8,8]
for i in range(len(e)):
    print("month",(i+1),"expense",e[i])
#output
#month 1 expense 3
#month 2 expense 5
#month 3 expense 6
#month 4 expense 7
#month 5 expense 8
#month 6 expense 8
for i in range(1,15):
    if(1%2==0):
        continue
    else:
        print(i*i)
#output
#1
#4
#9
#16
#25
#36
#49
#64
#81
#100
#121
#144
#169
#196
i=1
while i<=5:
    print(i)
    i=i+1
#1
#2
#3
#4
#5

