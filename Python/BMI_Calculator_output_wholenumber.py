height = float(input("Enter your height in m:"))
weight = float(input("Enter your weight in kg:"))
#print(type(height))
#print(type(weight))
BMI= weight/height**2
BMI_as_int = int(BMI)
print(BMI_as_int)