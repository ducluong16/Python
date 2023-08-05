age = (input("What is your current age? "))
age_as_int = int(age)
year_remaining = 90 - age_as_int
month_remaining = 12 * year_remaining
day_remaining = 30 * month_remaining
print("You have " + str(day_remaining) + " days, " +
      str(month_remaining) + " months, and " + str(year_remaining) + " year")
