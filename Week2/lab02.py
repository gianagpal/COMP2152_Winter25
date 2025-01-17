
#define the choices array
choices=["Rock", "Paper", "Scissors"]

def main():
    user_input=input("Enter your choice(Rock/paper/scissors): ").capitalize()

    if user_input not in choices:
        raise ValueError("Invalid choice! Please enter 'Rock', 'Paper' or 'Scissors'.")
    return user_input


#Run the game
if __name__ == "__main__":
    main()