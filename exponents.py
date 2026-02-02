import random
import time

# Converts powers of 2 to simplified number-letter pairs
def convertToLatin(num):
    if num < 10:
        return str(2**num)
    elif num < 20:
        return str(2**int(num - 10)) + "K"
    elif num < 30:
        return str(2**int(num - 20)) + "M"
    elif num < 40:
        return str(2**int(num - 30)) + "B"
    elif num < 50:
        return str(2**int(num - 40)) + "T"
    else:
        return None
    
# Quizzes the user on powers of 2 from 2^0 to 2^49
def quiz(A):
    incorrects = 0
    start = time.time()
    for i in range(len(A)):
        ans = convertToLatin(A[i])
        user_ans = input(f"What is 2 ** {A[i]}? ")
        if user_ans != ans:
            wrong = True
            incorrects += 1
            while wrong:
                user_ans = input("Wrong! Try again: ")
                if user_ans == ans:
                    wrong = False
                incorrects += 1
    end = time.time()
    print(f"Your total time was {(end - start):.0f} seconds. You missed {incorrects}.")

def main():
    exponents = [i for i in range(50)]
    random.shuffle(exponents)
    quiz(exponents)

if __name__ == "__main__":
    main()
