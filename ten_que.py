dict={'Alex':['subj1', 'subj2', 'subj3'], 
      'David': ['subj1', 'subj2']
          }
total=0
for value in dict:
    value_list=dict[value]
    count=len(value_list)
    total+=count
print(total)