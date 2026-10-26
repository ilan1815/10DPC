#Default methods in list

fruits=['mango','jackfruit','pineapple','apple']
print(fruits);

#add
fruits.append("pomagranate")
fruits.insert(3,'cherry')
fruits.extend(['melon','banana',"cherry"])

#remove
fruits.remove('melon')
fruits.pop(6)

#check index value & Count
print(fruits.index("cherry"))
print(fruits.count("cherry"))

#ordering
fruits.sort()
fruits.reverse()

#duplicate & clear
print(fruits.copy())
print(fruits.clear())


print(fruits)