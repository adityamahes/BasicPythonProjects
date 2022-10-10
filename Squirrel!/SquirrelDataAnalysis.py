import pandas
data = pandas.read_csv("2018SquirelData.csv")
column = data["Primary Fur Color"]
num_of_grey = len(data[column == "Gray"])
num_of_red = len(data[column == "Cinnamon"])
num_of_black = len(data[column == "Black"])

column_age = data["Age"]
num_of_adult = len(data[column_age == "Adult"])
num_of_juvenile = len(data[column_age == "Juvenile"])
num_of_NAN = len(data[column_age == "NaN"])

num_dict = {
    "Fur Color": ["Gray", "Red", "Black"],
    "Count": [num_of_grey, num_of_red, num_of_black],
}

age_dict = {
    "Age": ["Adult", "Juvenile", "NotCalculatable"],
    "Count": [num_of_adult, num_of_juvenile, num_of_NAN]
}

dict = pandas.DataFrame(num_dict)
csv = dict.to_csv()

with open("SquirrelCount.csv", mode="w") as file:
    file.write(csv)

age_csv = pandas.DataFrame(age_dict).to_csv()

with open("SquirrelAgeCount.csv", mode="w") as file:
    file.write(age_csv)
