#A >= 0.8 B >= 0.7 C >= 0.6 D < 0.6 F
score = input("Enter your score: ")
try:
    if float(score) < 1.0:
        if float(score) >= 0.9:
            print("A")
        elif float(score) >= 0.8:
            print("B")
        elif float(score) >= 0.7:
            print("C")
        elif float(score) >= 0.6:
            print("D")
        elif float(score) < 0.6:
            print("F")
    else:
        print("Uhu, not a great score!")     
except:
    print("Uhu, not a great score!")
