temp = int(input("What's the temperature outside? "))
cond = input("Is it sunny? (Y/N): ")

if temp > 28 and cond == "Y":
    print("It is hot and sunny")
elif temp < 10 and cond == "Y":
    print("It is cold and sunny")
elif temp > 28 and cond != "Y":
    print("It is hot and dark")
elif temp < 10 and cond != "Y":
    print("It is cold and dark")
elif 10 <= temp <= 28 and cond == "Y":
    print("It is nice weather")
else:
    print("It is cloudy or neutral weather")