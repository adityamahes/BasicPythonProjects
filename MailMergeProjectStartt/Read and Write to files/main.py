
with open("/Users/mahes/Desktop/my_file.txt") as file:
    contents = file.read()
    print(contents)

with open("../../Desktop/my_file.txt") as file:
    contents = file.read()
    print(contents)


with open("/Users/mahes/Desktop/my_file.txt", mode="w") as file:
    file.write("\nNewText\n123123123")


