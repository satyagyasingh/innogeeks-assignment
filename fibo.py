#fibonacci
i=0
j=1
print(i)
print(j)
for x in range(1,9,1):
    k=i+j
    i=j
    j=k
    print(k)