#Coding Questions


weapons=["Fist", "Knife", "Club", "Gun", "Bomb", "Nuclear bomb"]
def main():
    try:
        weaponRoll=int(input("Roll the dice(Choose 1-6): "))
        print("You chose "+weapons[weaponRoll])
        if weaponRoll<=2:
            print("You rolled a weak weapon, friend")
        elif weaponRoll<=4:
            print("Your weapon is meh")
        else:
            print("Nice weapon, friend!")

        if weaponRoll!=1:
            print("Thank goodness you didn't roll the Fist...")
    except ValueError:
        print("Enter an integer between 1 and 6")


if __name__ == "__main__":
    main()