def game():
    from art import TipCalculatorLogo as logo
    print(logo)
    print("Welcome to the tip calculator.")
    bill = float(input("What was the total bill? "))
    tip_percentage = (float(input("What percentage tip would you like to give? ")))/100
    people = float(input("How many people to split the bill? "))

    pay = round((bill * (1+tip_percentage))/people, 2)
    print(f"Each person should pay: ${pay}")