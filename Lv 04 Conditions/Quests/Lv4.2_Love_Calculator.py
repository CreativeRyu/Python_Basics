# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
name1 = name1.lower()
name2 = name2.lower()

resultT = name1.count("t") + name2.count("t")
resultR = name1.count("r") + name2.count("r")
resultU = name1.count("u") + name2.count("u")
resultE = name1.count("e") + name2.count("e")

resultL = name1.count("l") + name2.count("l")
resultO = name1.count("o") + name2.count("o")
resultV = name1.count("v") + name2.count("v")
resultE2 = name1.count("e") + name2.count("e")

resultTRUE = resultT + resultR + resultU + resultE
resultLOVE = resultL + resultO + resultV + resultE2

result = int(f"{resultTRUE}{resultLOVE}")

if result>= 90 or result <= 10:
    print(f"Your score is {result}, you go together like coke and mentos.")
elif result < 50 and result > 40:
    print(f"Your score is {result}, you are alright together.")
else:
    print(f"Your score is {result}.")