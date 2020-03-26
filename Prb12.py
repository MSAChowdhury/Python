#Rewrite the grade program from the previous chapter using a function called computegrade that takes a score as its parameter and returns a grade as a string.
def comptegrade(score):
    try:
        if float(score) < 1.0:
            if float(score) >= 0.9:
                str = "A"
            elif float(score) >= 0.8:
                str = "B"
            elif float(score) >= 0.7:
                str = "C"
            elif float(score) >= 0.6:
                str = "D"
            elif float(score) < 0.6:
                str = "F"
        else:
            str = "Uhu, not a great score!"
    except:
        str = "Uhu, not a great score!"
    return str

score = input("Enter your score: ")
print(comptegrade(score))
