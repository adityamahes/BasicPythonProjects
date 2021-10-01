def game():
    import random
    # from replit import clear
    from art import HeadsOrTailsLogo as logo
    print(logo)
    print("Welcome to CoinFlip")
    continuei = True
    while continuei:
        counth = 0
        countt = 0
        times = int(input("Enter how many times you want to CoinFlip: "))
        for x in range(times):
            random_side = random.randint(0, 1)
            if random_side == 1:
                print(f"{x + 1}: You got Heads")
                counth += 1
            else:
                print(f"{x + 1}: You got Tails")
                countt += 1
        print(f"Here is your record of flips: \n Number of heads: {counth} \n Number of tails: {countt}")
        if input("Do you want to play again? (y,n): ") != 'y':
            continuei = False
            print("See you again later")
        # else:
            # clear()
