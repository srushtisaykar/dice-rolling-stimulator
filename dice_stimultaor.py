import random

def roll_dice():
    /*Simulates rolling a dice and returns the result.*/
    return random.randint(1, 6)

def main():
    print("Welcome to the Dice Simulator!")

    while True:
        input("Press Enter to roll the dice...")

        dice_result = roll_dice()
        
        print("The dice rolled and you got:", dice_result)

        play_again = input("Do you want to roll again? (yes/no): ")
        if play_again.lower() != "yes":
            print("Thank you for playing!")
            break

if __name__ == "__main__":
    main()
