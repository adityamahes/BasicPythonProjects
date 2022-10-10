import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
new_dict = {row.letter: row.code for (index, row) in data.iterrows()}


def generate_phonetic():
    user_input = input("Enter a word: ")
    try:
        output = [new_dict[letter.upper()] for letter in user_input]
    except KeyError:
        print("Sorry only letters the alphabet please")
        generate_phonetic()
    else:
        print(output)


generate_phonetic()
