#median of three
i=int (input("first"))
j=int (input("second"))
k=int (input("third"))
x=i
y=j
z=k
if(j>x):
    x=j
    y=i
    z=k
if(k>x):
    x=k
    y=j
    z=i
if(y>z):
    print(y)
else:
    print(z)
