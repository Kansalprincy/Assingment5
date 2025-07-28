result = {'Abhay':50,'Shiv':49,'Advyth':50,'Pankaj':50,'Princy':50}
name = input("Enter the name: \n")
if (name == "Abhay"):
    print(result.get("Abhay"))
elif (name == "Shiv"):
    print(result.get("Shiv"))
elif (name == "Advyth"):
    print(result.get("Advyth"))
elif (name == "Pankaj"):
    print(result.get("Pankaj"))
elif (name == "Princy"):
    print(result.get("Princy"))
else :
    print("Student not found")