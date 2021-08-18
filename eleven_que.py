my_dict = {'a':50, 'b':58, 'c':56,'d':40, 'e':100, 'f':20}
list=[] 
max1=0
max2=0
max3=0
for i in my_dict:
    for j in my_dict:
        if my_dict[j]>max1:
            max1=my_dict[j]
        elif max1>my_dict[j] and max2<my_dict[j]:
            max2=my_dict[j]
        elif max3<my_dict[j] and max2>my_dict[j]:
                max3=my_dict[j]
list.append(max1)
list.append(max2)
list.append(max3)
print(list)

