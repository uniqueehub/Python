f=open("C:/Code/PycharmProjects/Python/funny.txt","w")
f.write("I am Learning")
f.write("\nI am Learning Chinese")
f.close()
f=open("C:/Code/PycharmProjects/Python/funny.txt","a")
f.write("\nI am Learning Hindi")
f.write('''\nJohny, Johny!
Yes, Papa
Eating sugar?
No, Papa
Telling lies?
No, Papa
Open your mouth!
Ha! Ha! Ha!''')
f.close()
###reading file line by line
##count number of words
f=open("C:/Code/PycharmProjects/Python/funny.txt","r")
f_out=open("C:/Code/PycharmProjects/Python/funny_wc.txt","w")
for i in f:
    tokens=i.split(' ')#split() will split the string using input chracter and return a list(array) of words.
    #print(i)
    #print(str(tokens))
    f_out.write("wordcount: "+str(len(tokens))+" "+i)
    #print(len(tokens))
f.close()