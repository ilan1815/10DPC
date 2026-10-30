#set

skills={'java','python','react','java'}

print(skills)

required={'java','sql'}

#common (&)

common=skills & required

print(common)

#frozen set
frozen=frozenset(skills)
print(frozen)

#use frozen set in a loop
for skill in frozen:
    print(skill)
    
#with index using (enumerate())
for index, skill in enumerate(frozen):
    print(f"Index {index}:{skill}")

#set operations
a={1,2,3,4,5}
b={4,5,6,7,8}

#merge two sets
print(a|b)

#elements present in both
print(a & b)

#element present in a but not b
print(a-b)

#element present in either a or b but not in both
print(a^b)