#method1
k=input("enter the sentence")
x=k.upper()
n=len(x)
V=[]
for i in range(0,n):
    if x[i]=='A'or x[i]=='E'or x[i]=='I'or x[i]=='O'or x[i]=='U':
        if x[i] not in V:
            V.append(x[i])
           
count=[]          
for i in range(0,len(V)):
    c=0
    for j in range(0,n):
        if V[i]==x[j]:
            c=c+1
    count.append(c)
print("Vowels in sentence--",V)
print("Each vovel is repeated as--",count,"(request with vowel)")

#method2
'''k=input("enter the sentence")
vowel=['A','E','I','O','U']
x=k.upper()
v=[]
for letter in x:
    if letter in vowel:
        if letter not in v:
            v.append(letter)
count=[]
print("Vowels in sentence--",v)
for i in v:
    c=0
    for j in range(0,len(x)):
        if x[j]==i:
            c=c+1
    count.append(c)        

print("Each vowel is repeated as--",count,"(request with vowel)")'''
