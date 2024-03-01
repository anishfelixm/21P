import random

def main():
    choices = ["rock", "paper", "scissors"]
    u_wins, comp_wins = 0, 0

    while True:
        u_guess = input("Enter Rock/Paper/Scissors or Q/q to quit: \n").lower()
        
        if u_guess == "q":
            break

        if u_guess not in choices:
            continue

        comp_guess = random.choice(choices)

        if u_guess == "rock" and comp_guess == "paper":
            print("You win!")
            u_wins += 1
        elif u_guess == "paper" and comp_guess == "scissors":
            print("You win!")
            u_wins += 1
        elif u_guess == "scissors" and comp_guess == "rock":
            print("You win!")
            u_wins += 1
        else:
            print("You lost!")
            comp_wins += 1
    
    print("You won", u_wins,"times")

if __name__ == "__main__":
    main()