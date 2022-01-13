print("╔══════════════════╗")
print("   ଐତିହାସିକ ବାଲିଯାତ୍ରା  ")
print("╚══════════════════╝")
height = int(input("Please enter your height in centimeter. \n"))
bill = 0
# Height check for customer above 120cm can ride
if height > 120:
    print("You can take the ride")
    # Separate charges for age groups in $
    age = int(input("Please enter your age. \n"))
    if age <= 12:
        bill = 5
    elif age < 18:
        bill = 7
    elif age >= 45 and age <= 55:  # Free Ride for midlife crisis people
        print("As you are going through midlife crisis, you can take free ride")
    else:
        bill = 12
    # Additional $3 charges for Photo
    extra = input("Do you want an extra photo of this ride which will cost you $3 additional ? Y or N \n")
    if extra == "Y":
        print(f"You have to pay only ${bill + 3}")
    else:
        print(f"You have to pay only ${bill}")
else:
    print("You are too small to take this ride")
