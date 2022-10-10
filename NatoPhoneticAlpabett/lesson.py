# List Comprehension (unique to python language)


# List comprehension is when you create a new list from a previous list
    # You can use a For Loop to do so
    # (in this example adding one to each element)
numbers = [1, 2, 3]
new_list = []
for n in numbers:
    add_1 = n + 1
    new_list.append(add_1)
    # But there is a better way (list comprehension)
        # This is the structure (new_list = [new_item for item in list])
        # You have to replace the placeholders with the values
        # Ex:
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
new_list = [n+1 for n in numbers]
# This can work with alll types of sequences
    # list
    # range
    # string
    # tuple

# Conditional List comprehensions
# The model is similar but with 2 more keywords
# new_list = [new_item for item in list if test]
    # This only adds the new item, if the test passes (boolean)
    # Example:
names = ["Abcd", "Bcde", "Cdefgh", "Defghijkl", "Efgh", "Fghijkl"]
# I only want the names that are 4 letters or less
short_names = [name for name in names if len(name) < 5]
print(short_names)  # ---> ['Abcd', 'Bcde', 'Efgh']
    # Example 2
longer_names = [name.upper() for name in names if len(name) > 5]  # --> ['CDEFGH', 'DEFGHIJKL', 'FGHIJKL']



# Dictionary Comprehension
    # This is the structure (optional: make it conditional)
        # new_dict = {new_key:new_value for item in list(any iterable)}
        # To take values from existing dictionary:
            # new_dict = {new_key:new_value for (key, value) in dict.items()}
            # The items() turns the key value pair into a tuple
names = ['Mark', 'Amber', 'Todd', 'Anita', 'Sandy']
# new_dict = {new_key:new_value for item in list(any iterable)}
import random
students_scores = {student: random.randint(1, 100) for student in names}
print(students_scores)
# new_dict = {new_key:new_value for (key, value) in dict.items()}
passed_students = {key: value for (key, value) in students_scores.items() if value >= 60}
print(passed_students)




# How to iterate over  pandas data frame
student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}
# It is easy to iterate over a dictionary:
for (key, value) in student_dict.items():
    print(key)
    print(value)

# You can loop through a data frame the same way you loop through a dictionary
# Pretty much like python dictionary
import pandas
student_DataFrame = pandas.DataFrame(student_dict)
# print (student_DataFrame)
for (key, value) in student_DataFrame.items(): # Loop through columns
    print(key) # Gives a header
    print(value) # Gives the data for the header
    # Not very useful, we didn't want this
# Therefore instead of items() we use iterrow() to loop through rows.
for (key_or_index_corresponds_to_the_number, value_or_row) in student_DataFrame.iterrows():
    print(key_or_index_corresponds_to_the_number)
    print(value_or_row) # series object
    # so...
    print(value_or_row.student)
