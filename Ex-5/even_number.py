total = 0
for number in range(2, 101, 2):
    old_total = total
    total += number
    # print(f"{number} + {old_total} = {total}")
print(f"Total: {total}")

total2 = 0
for number in range(1, 101):
    if number % 2 == 0:
        old_total = total2
        total2 += number
        # print(f"{number} + {old_total} = {total}")
print(total2)
        
    