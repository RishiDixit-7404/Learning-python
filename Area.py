import math
choice = int(input("Enter your choice "))
if choice == 1:
    d1 = int(input("enter the dimension "))
    d2 = int(input("enter the dimension "))
    print(d2*d1)
elif choice == 2:
    d1 = float(input("enter the radius "))
    print(math.pi * d1 * d1)