# 🚨 Don't change the code below 👇
row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# 🚨 Don't change the code above 👆
 
#Write your code below this row 👇
print(f"Du hast {position} gegeben")
goto_row = []
goto_ort =  "💰"
match position[1]:
    case "1":
        goto_row = row1
    case "2":
        goto_row = row2
    case _:
        goto_row = row3
match position[0]:
    case "1":
        goto_row[0] = goto_ort
    case "2":
        goto_row[1] = goto_ort
    case _:
        goto_row[2] = goto_ort
 
 
#Write your code above this row 👆
 
# 🚨 Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}")
 