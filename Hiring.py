#Do not CopyRight
#PA

print("--------------------")
print("Write your Information")
name = input(str("Name="))
last_name = input(str("Last name="))
Age = int(input("Your Age="))
if Age>=18:
    print("--------------------")
elif Age<18:
    print("--------------------")
    print("Sorry you are under 18")
    exit()
print("Do you have python degree?")
print("""1-Yes
2-No""")
degree = input("=>")
if degree in ["yes" , "Yes" , "1"]:
    print("--------------------")
elif degree in ["no" , "No" , "2"]:
    print("--------------------")
    print("Sorry You cannot be hired")
    exit()
else:
    print("--------------------")
    print("invalid answer")
    exit()
print("Send your URL degree")
URLdegree = input("=>")
print("--------------------")
print("Info send to manager.\nWait for reply from 0912*******")
print("--------------------")
print("Creator:PA")
print("--------------------")