weight = int(input("What is your weight:"))
unit = input(" L(lbs) or K(kgs)")
if unit.upper()== "L":
    convert=weight*0.45
    print(f"Your weight is {convert}kgs")
elif unit.upper() == "K":
    convert=weight/0.45
    print(f"Your weight is {convert}lbs")
else:
    print(" Entered Value is Wrong")
