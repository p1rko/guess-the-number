import random

secret = random.randint(1, 30)
attempts = 0
highscore = 100
username= None

with open("highscore.txt", "r", encoding="UTF8") as results_file:
    results = results_file.read().split()
    for i in range(len(results)):
        if results[i].isdigit() == True:
            if int(results[i]) < highscore:
                highscore = int(results[i])
                username = results[i-2]
    print("Currently {0} has the highscore with {1} guesses".format(username, highscore))

name = input("Enter username (illegal characters include space): ")

while True:
    guess = int(input("Guess the secret number "))
    attempts +=1
    if guess == secret:
        print("Congrats my g it took you {0} attempts".format(attempts))
        with open("highscore.txt", "a", encoding="UTF8") as score:
            score.write("{0} took {1} attempts".format(name, attempts) + "\n")
        break
    elif guess < secret:
        print("Just not high enough")
    elif guess > secret:
        print("Try something lower")
