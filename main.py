print("Welcome to School Survival!")
name = input("What is your name? ")

score = 0

print()
print("Hi " + name + "! Your goal is to survive the school day.")
print("You wake up late and need to get to school.")

choice1 = input("Do you take the bus, walk, or ask for a ride? ")

if choice1 == "bus":
    print("The bus is late, but you make it to school.")
    score = score + 1

elif choice1 == "walk":
    print("You get some exercise, but you arrive sweaty and tired.")
    score = score - 1

elif choice1 == "ride":
    print("You get to school quickly and have time to relax.")
    score = score + 2

else:
    print("That was not one of the choices. You got confused and missed homeroom.")
    score = score - 2


print()
print("Now you have a quiz in science class.")
choice2 = input("Do you study, guess, or ask a friend for help? ")

if choice2 == "study":
    print("Good choice! You feel prepared for the quiz.")
    score = score + 2

elif choice2 == "guess":
    print("You guess on most of the questions. Risky move.")
    score = score - 1

elif choice2 == "help":
    print("Your friend explains the topic quickly. You understand enough to pass.")
    score = score + 1

else:
    print("You did nothing and stared at the wall.")
    score = score - 2


print()
print("At lunch, you see a mysterious glowing sandwich.")
choice3 = input("Do you eat it, throw it away, or show a teacher? ")

if choice3 == "eat":
    print("Bad idea. You gain super speed, but only for 3 seconds.")
    score = score - 1

elif choice3 == "throw":
    print("You throw it away and save the cafeteria.")
    score = score + 1

elif choice3 == "teacher":
    print("The teacher calls the science department. You become a school hero.")
    score = score + 3

else:
    print("You ignore it. The sandwich escapes.")
    score = score - 2


print()
print("Your final score is:", score)

if score >= 5:
    print("Ending: Legendary Student!")

elif score >= 2:
    print("Ending: Pretty Good Day!")

elif score >= 0:
    print("Ending: Barely Survived the Day.")

else:
    print("Ending: Detention Speedrun.")
