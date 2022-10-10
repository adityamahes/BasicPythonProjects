# # ERRORS
# # FileNotFound
# with open("a_file.txt") as file:
#     file.read()
#
# # KeyError
# a_dictionary = {"Key": "value"}
# value = a_dictionary["non_existent_key"]
#
# # IndexError
# fruit_list = ["Apple", "Banana", "Pear"]
# fruit = fruit_list[3]
#
# #TypeError
# text = "abc"
# print(text + 5)

# When something goes wrong, we can catch the error, it doesn't die catastrophically
# Handling exceptions
'''
try: # Something that might cause an error
except: # Do this if there was an error
else:  # Do this if there was no error
finally: # Do this no matter what happens
'''

# Catching the file not found error or exception
try:
    file = open("a_file.txt")  # Will cause an error
    a_dictionary = {"Key": "value"}
    print(a_dictionary["Key"])
except FileNotFoundError: # We should specify which error to expect
    # (because the try block can have a different error that we neve expected)
    file = open("a_file.txt", mode="w") # If it does cause an error do this
    # Creates a file
except KeyError as error_message: # with the error_message we can get hold of the error message
    # Without specifying the error, the except block will catch all types of errors
    print(f"That key does not exist: {error_message}")
# There are no errors. We are catching the exceptions
else: # If there were no exceptions... If the file didn't exist it will never execute this block
    contents = file.read()
    print(contents)
finally: # Does his anyway. Nothing matters if it succeeded or failed.
    file.close()
    print("File was closed")
    raise KeyError("This is an error that I made up")

# We can also use the keyword raise:  to raise our own errors or exceptions
# You have to raise a known Error class


# JSON Javascript Object Notation
# Basically nested lists and dictionaries
# To work with JSON we use the inbuilt JSON library

# import json
# with open("Manager.json", mode="r") as file:
#     # Reading Data (old data in this case)
#     data = json.load(file)  # Reads from the json file
#     # The file path is the only required input
#     # Data is a python dictionary. We can use dump and load to switch between python dictionaries and json data
#
#     # Updating with new data
#     data.update(new_data)  # It didn't add it, it updated it
#
# with open("Manager.json", mode="w") as file:
#     # Writing data in file (saving updated data in this case)
#     json.dump(new_data, file, indent=4)  # Input data is a dictionary
#     # The required arguments include:
#     # the data you want to keep (dictionary),
#     # the file to put it in,
#     # many optional stuff. for instance indent which makes it easier for people to read.
