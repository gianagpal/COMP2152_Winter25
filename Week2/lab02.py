import random
#define the choices array
choices=["Rock", "Paper", "Scissors"]

def main():
    try:
        user_input=input("Enter your choice(Rock/paper/scissors): ").capitalize()

        #Validate user input
        if user_input not in choices:
            raise ValueError("Invalid choice! Please enter 'Rock', 'Paper' or 'Scissors'.")

        #Convert the user input to an index
        player_choice=choices.index(user_input)

        #randomly select computer choice
        computer_choice=random.randint(0,2)

        print(f"Player Choice: {choices[player_choice]}")
        print(f"Computer Choice: {choices[computer_choice]}")

        #determine the winner
        if player_choice == computer_choice:
            print("It's a tie")
        elif (player_choice == 0 and computer_choice == 2) or \
                (player_choice == 1 and computer_choice == 0) or \
                (player_choice == 2 and computer_choice == 1):
            print("Player wins!")
        else:
            print("Computer wins!")
    except ValueError as e:
        print("Error {e}")

    return True


#Run the game
if __name__ == "__main__":
    main()