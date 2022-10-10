def game():
    from art import LoveCalculatorLogo as logo
    print(logo)
    print("Welcome to the Love Calculator! The closer your score is to 50 ==> Love")
    name1 = input("What is your name? \n")
    name2 = input("What is their name? \n")
    name = name1.lower() + name2.lower()
    t = name.count('t')
    r = name.count('r')
    u = name.count('u')
    e = name.count('e')
    l = name.count('l')
    o = name.count('o')
    v = name.count('v')
    e = name.count('e')
    true = t+r+u+e
    love = l+o+v+e
    loveScore = int(str(true)+str(love))
    if loveScore <= 10 or loveScore >= 90:
        print(f'Your score is {loveScore}, you go together like coke and Mentos.')

    elif 40 <= loveScore <= 60:
        print(f'Your score is {loveScore}, you are alright together.')

    else:
        print(f'Your score is {loveScore}.')