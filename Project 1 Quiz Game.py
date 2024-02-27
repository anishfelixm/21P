def main():
    print("Welcome to the Quiz\n\n")

    play = input("Do you want to continue? [y/n]").strip().lower()

    if play != "y":
        quit()
    
    print("\n\nLets Play !! :)")
    score = 0
    
    # Question 1
    answer = input("\n\nWhat does CPU stand for? \n").strip().lower()

    if answer == "central processing unit":
        score += 1
        print("Correct! Score :", score)
    else:
        print("Wrong! Score :", score)
    
    # Question 2
    answer = input("\n\nWhat does GPU stand for? \n").strip().lower()

    if answer == "graphics processing unit":
        score += 1
        print("Correct! Score :", score)
    else:
        print("Wrong! Score :", score)

    # Question 3
    answer = input("\n\nWhat does RAM stand for? \n").strip().lower()

    if answer == "random access memory":
        score += 1
        print("Correct! Score :", score)
    else:
        print("Wrong! Score :", score)
    
    # Question 4
    answer = input("\n\nWhat does PSU stand for? \n").strip().lower()

    if answer == "power supply":
        score += 1
        print("Correct! Score :", score)
    else:
        print("Wrong! Score :", score)
    
    print("Final Score :", (score * 100) // 4, "%")

if __name__ == "__main__":
    main()