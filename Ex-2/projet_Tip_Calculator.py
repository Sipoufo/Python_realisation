print("Welcome to tip calculator")
total_Bill = float(input("What was the total bill? $"))
percentage = int(input("What percentage tip would you like to give ? 10, 12 or 15 ? "))
people = int(input("How many people to spilt the bill ? "))

# percentage
final_Percentage = total_Bill + ((total_Bill * percentage)/100)
#Split
split_Bill = final_Percentage / people
#Round
#round_Split_Bill = round(split_Bill, 2)
round_Split_Bill = "{:.2f}".format(split_Bill)

print(f"Each person should pay: ${round_Split_Bill}")