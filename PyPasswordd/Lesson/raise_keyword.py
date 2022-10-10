# BMI
height = float(input("Height: "))
weight = float(input("Weight: "))

if height > 3:
    raise ValueError("Human height should not be over 3 meters. ")
# Means that there is a problem with the content of the object you tried to assign value to.
# We use this when the code is perfectly ok but not ok
bmi = weight / height ** 2
print(bmi)