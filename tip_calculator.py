print("Welcome to tip calculator")
bill = float(input("What wax the total bill? $"))
percent = float(input("What percentage tip would you like to give? 10,12,or 15? "))
split = float(input("How many people to split the bill? "))

total = bill + (percent*bill)/100
per_person = round(total/split, 2)

print("Each person should pay: $",per_person)
