#Dictionary

students={'name':'karthick',
          'mark':88,
          'subject':'maths'}

#add new list in dict

students['class']=12

#update list element

students['mark']+=2

print(students)

candidate={'id':33, 'name':'harish'}
profile={"role":"software dev",'domain':"IT"}
details={'salary':500000, 'experience':'3 years'}

#merge two dictionaries
merged_dict=candidate|profile

print(merged_dict)

#update dict
details|=profile

print(details)
