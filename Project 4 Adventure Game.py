from random import randint

def main():
    name = input("Please Enter your name: ")
    print("Welcome", name, "to your adventure!")

    cur = input("\n\nYou are on a dirt road. You have 3 paths in front of you. One to your right, other to your left and one straight forward. Choose your path [left/right/forward]: ").lower()
    
    if cur == "left":
        cur = input("\nNow you have reached a river. You can swim across it or walk around it. Choose wisely [swim/walk]: ").lower()
        
        if cur == "swim":
            random = randint(0,999999)
            
            if random % 2 == 0:
                cur = input("\nCongratulations! You have now crossed the river. You now find a box in front of you. Do you break it? Choose wisely[break/leave]: ").lower()
                
                if cur == "break":
                    print("\n\nCongratulations! You found a trasure chest! You become rich!!")
                    quit()
                else:
                    print("\n\nYou have reached the other side. But you lost your money while swimming. Now you are poor! Sorry :(")
                    quit()
            else:
                print("\nOh no! You got eaten by a crocodile. You died. Sorry :(")
                quit()
        
        else:
            random = randint(0,999999)
            
            if random % 2 == 0:
                cur = input("\nCongratulations! You have now crossed the river. You now find a box in front of you. Do you break it? Choose wisely[break/leave]: ").lower()
                
                if cur == "break":
                    print("\n\nCongratulations! You found a trasure chest! You become rich!!")
                    quit()
                else:
                    print("\n\nYou have reached the other side. But you lost your money . Now you are poor! Sorry :(")
                    quit()
            else:
                print("\nOh no! You got robbed and killed by robbers. You died. Sorry :(")
                quit()

    elif cur == "right":
        cur = input("\nYou find a cave in front of you. It is cold outside. Do you go in? Choose wisely[go/ignore]: ").lower()
        
        if cur == "go":
            random = randint(0,999999)
            
            if random % 2 == 0:
                cur = input("\nWoah! Suddenly there was a violent storm. \nCongratulations! You found some shelter. Do you explore the cave? Choose wisely[yes/no]: ").lower()
                
                if cur == "yes":
                    print("\n\nCongratulations! You found a trasure chest! You become rich!!")
                    quit()
                else:
                    print("\n\nYou are waiting for the storm to end. Suddenly a bear comes in front of you! It attacks you and you die. Sorry :(")
                    quit()
            else:
                print("\nOh no! There is a bear inside the cave. The bear kills you and eats your body. You died. Sorry :(")
                quit()
        
        else:
            random = randint(0,999999)
            
            if random % 2 == 0:
                cur = input("\nYou now find a box behind a tree near the house. Do you go for it? Choose wisely[yes/no]: ").lower()
                
                if cur == "yes":
                    cur = input("Wow! There's a treasure chest behing this tree. Do you break it? [break/ignore]")
                    
                    random = randint(0,999999)
                    if random % 2 == 0:
                        if cur == "break":
                            print("\n\nCongratulations! You found a trasure chest! You become rich!!")
                            quit()
                        else:
                            print("\n\nYou find nothing. Now it's extremely cold and you can't walk into the cave for protection. You die. Sorry :(")
                    else:
                        print("\n\nOh no! Look up!! There's a bear on the tree. It attacks you and you die. Sorry! :(")
                        quit()
                
            else:
                print("\nIt became extremely cold and you died of frostbite. Sorry :(")
                quit()
            
    elif cur == "forward":
        print("You took the easiest route! You looser... try some risk next time. BOOOOO!!!")
    
    else:
        print("You left your adventure!")
        quit()

if __name__ == "__main__":
    main()