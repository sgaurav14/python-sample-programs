user_weight = int(input("Enter your weight: "))
unit = input("(L)bs of (K)gs")

if unit.upper() == "L":
    converted = user_weight * 0.45
    print(f"You are {converted} kilos")
else:
    converted = user_weight / 0.45
    print(f"You are {converted} pounds")