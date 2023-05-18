age = input("What is your current age?")
my_age=int(age)
cap_year=int(90)
totalyearsihave = cap_year - my_age
totaldaysihave = totalyearsihave * 365
totalweeksihave = totalyearsihave * 52
totalmonthsihave = totalyearsihave * 12
message = f"You have {totaldaysihave} days, {totalweeksihave} weeks, and {totalmonthsihave} months left."
print(message)