from random import randint

def roll():
    return randint(1,6)

def main():
    players = 0
    while True:
        try:
            players = int(input("Enter the number of players(2-4): "))
            if 2 <= players <= 4:
                break
        except ValueError:
            print("Enter a number")
            pass
    
    Scores = [0 for _ in range(players)]
    Top_limit = 10

    while max(Scores) < Top_limit:
        for i in range(players):
            cur_score = 0
            print("\n\nPlayer", i+1, "'s turn")
            print("Your current score:", Scores[i], "\n")
            
            while True:
                ch = input("Would you like to roll(y)?").rstrip().lower()
                
                if ch != "y":
                    break
                
                new_roll = roll()

                if new_roll == 1:
                    print("You rolled a 1! Turn done!")
                    cur_score = 0
                    break
                
                cur_score += new_roll
                print("You rolled a", new_roll)
                print("Your score:", cur_score)

            Scores[i] += cur_score
            print("Player", i, "Score: ", cur_score)
    
    max_score = max(Scores)
    winner = Scores.index(max_score)
    print("Player", winner+1, "is the winner!\nScore:", Scores[winner])

if __name__ == "__main__":
    main()