age = int(input("Enter your current age? "))

years_remaining = 90 - age

days = years_remaining * 365
weeks = years_remaining * 52
months = years_remaining * 12

print(f"You have {days} days, {weeks} weeks and {months} months left")