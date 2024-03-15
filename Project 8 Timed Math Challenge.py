from random import randint, choice
import time

TOTAL_NO_OF_PROBLEMS = 10
MIN_NUMB = 1
MAX_NUMB = 10
OPERATORS = ["+", "-", "*"]

def generate_problem():
    f_num = randint(MIN_NUMB, MAX_NUMB)
    l_num = randint(MIN_NUMB, MAX_NUMB)
    op = choice(OPERATORS)
    
    exp = f"{f_num} {op} {l_num}"
    ans = eval(exp)
    
    return exp, ans

def main():
    wrong = 0

    input("Press Enter to start!!")
    print("----------------------")

    start_time = time.time()
    
    for i in range(TOTAL_NO_OF_PROBLEMS):
        exp, ans = generate_problem()
        while True:
            usr_ans = input("Problem #" + str(i + 1) + ": " + exp + " = ")
            if usr_ans == str(ans):
                break
            wrong += 1
    
    end_time = time.time()
    print("----------------------")

    time_taken = round(end_time - start_time, 1)

    print("Well Done! You Finished in", time_taken, "seconds and made", wrong, "mistakes.")

if __name__ == "__main__":
    main()