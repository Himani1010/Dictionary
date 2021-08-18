list1=["one","two","three","four","five"]
list2=[1,2,3,4,5,]
empty={}
for i in range (0 ,len(list1)):
    for j in range (0,len(list2)):
        empty[list1[i]]=list2[i]
print(empty)