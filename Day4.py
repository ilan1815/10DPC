#For Loop

for i in range(1,20):
    print(i)
    
#list 

nthg=['ilan','kamal',20,9]

for i in nthg:
    print(i)
    
#dict

emp={"id":00,
      "name":"anbu"}

for key in emp:
    print(key)
    print(emp["id"])
    
for value in emp.values():
    print(value)
    
for key, value in emp.items():
    print(key,":",value)

#list to dict

fruits = ["apple", "banana", "orange"]

my_dict={}

for i in range(len(fruits)):
    my_dict[i]=fruits[i]
    print(my_dict)
    
names = ["Ilan", "Kamal", "Arun"]
ages = [22, 23, 21]

my_dict1={}

for i in range(len(names)):
    my_dict1[names[i]]=ages[i]
    print(my_dict1)