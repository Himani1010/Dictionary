my_dict = {
    'a':50, 
    'b':58,
    'c': 56,
    'd':40,
    'e':100, 
    'f':20
    }
list1=[]
max1=0
max2=1
max3=0
for i in my_dict:
    for j in my_dict:
        if list1[j]>max1:
            max1=list1[i]
        if max1>list1[j] and max2<list1[j]:
            max2=list1[j]
            if max3<max2 and max3<max1:
                max3=list1[j]
        j=j+1
print(max1,max2,max3)
print(list1)

