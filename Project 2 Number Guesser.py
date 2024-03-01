import random

def main():
    while True:
        try:
            limit =  int(input("Type a Number: "))
            if limit <= 0:
                print("Enter number greater than 0 \n")
                raise ValueError
            break
        except ValueError:
            pass
    
    numb1 = random.randint(0, limit)
    guesses = 0
    
    while True:
        u_numb = 0
        
        while True:
            try:
                u_numb = int(input("Your Guess? "))
                break
            except ValueError:
                continue
        
        guesses += 1
        
        if u_numb == limit:
            print("Correct !")
            break
        elif u_numb > limit:
            print("Guess lower..")
        else:
            print("Guess higher..")
    
    print("You got it in", guesses, "guesses!")

if __name__ == "__main__":
    main()