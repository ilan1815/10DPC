#Conditional Statement

"""
mark=int(input("Enter you 10th Mark: "))

if mark >= 90 :
  print("A+")
elif mark >=80 :
 print("b+")
elif mark >=70 :
 print("C")
elif mark < 70 :
    print("Fail!!")
else:
    print("Enter a valid Mark")
"""
    
#Nested Condition

username=input("Enter Your username: ")
password=input("Enter Your Password: ")
if username == "Ilan" :
    if password == "Ilan@2004":
        print("Access Granted!!");
    else:
        print("Access Denied!!");
else:
    print("Please enter a valid Username & Password")
    
#Ternary condition

status="Password is Vallid" if password=="Ilan@2004" else "Password is invalid"
print(status);