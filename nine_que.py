a="MISSISSIPPI"
i=0
k=0
b=[]
d={}
while i<len(a):
    if a[i] not in b:
        b.update(a[i])
        j=1
        c=0
        while j<len(a):
            if b[k]==a[j]:
                c=c+1
            j=j+1
        d.update({a[i]:i})
        k=k+1
    i=i+1
print(d)