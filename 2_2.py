print("Welcome to the tip calculator")
bill = float(input("What is the total bill? "))
tip = float(input("What percentage tip would you like to give? "))
people = int(input("How many people to split the bill? "))
total_for_everyone = round(bill*(1+tip)/people, 2)
print(f"What is the amount each person has to pay? {total_for_everyone}")
