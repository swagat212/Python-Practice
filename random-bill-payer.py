# Split string method
import random
names_string = input("Give me everybody's names, separated by a comma.\n ")
names = names_string.split(",")
count = (len(names))
choice = random.randint(0,count - 1)
pay = names[choice]
print(f"{pay} have to pay the bill")

# Or we can use random.choice(name) to generate a random index from the list 
