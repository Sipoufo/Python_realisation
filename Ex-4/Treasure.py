row1 = ["⬜", "⬜", "⬜"]
row2 = ["⬜", "⬜", "⬜"]
row3 = ["⬜", "⬜", "⬜"]

map = [row1, row2, row3]

print(f"{row1}\n{row2}\n{row3}")

position = input("Where dp you want to put the treaseure ?")

map[int(position[0])-1][int(position[1])-1] = "❤"

print(f"{row1}\n{row2}\n{row3}")