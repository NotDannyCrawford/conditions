# CS104
# Daniel Crawford
# conditions.py
temp = "xzyz"
while temp != "end":
    temp = input("Please enter the current temperature: ")
    if temp == "end":
        break
    try:
        temp = int(temp)
    except ValueError:
        print("Please enter a valid number or type 'end' to exit")
        continue
    if temp > 90:
        print("Wear Shorts")
    elif temp > 70:
        print("Short sleeves are fine")
    elif temp > 50:
        print("Wear a jacket")
    elif temp > 32:
        print("Wear a heavy coat")
    elif temp <= 32:
        print("Stay Inside")
print("End of Program!")
