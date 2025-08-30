score = int(input("Enter your score: "))

if score >=90 and score <= 100:
 print("A")
elif score  >=80 :
    print ("B")
elif score >= 70 :
    print ("B-")
elif score >= 60 :
    print ("C")
else :
    print ("Fail")

    temp  = int(input("Enter your score: "))

    if not(temp >= 15 and temp <= 30):
        print("Weather is bad, stay inside")
    elif not(temp <= 0 and temp <= 50):
        print("Weather is good, Go outside")
