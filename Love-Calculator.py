print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

fullname = name1 + name2
lower_case = fullname.lower()
t = lower_case.count("t")
r = lower_case.count("r")
u = lower_case.count("u")
e = lower_case.count("e")
true = t + r + u + e

l = lower_case.count("l")
o = lower_case.count("o")
v = lower_case.count("v")
e = lower_case.count("e")
love = l + o + v + e

score = int(str(true) + str(love))

if score >= 10 and score <= 90:
    print(f"Your score is {score}, you got together like coke and mentos.")
elif score >= 40 and score <=50:
    print(f"Your score is {score}, and you are alright together")
elif score > 90:
    print(f"Your score is {score} and its impossible")
else:
    print(f"Your score is {score}")
