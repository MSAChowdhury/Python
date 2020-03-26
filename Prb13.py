#Write a program which repeatedly reads numbers until the user enters “done”. Once “done” is entered,
#print out the total, count, and average of the numbers. If the user enters anything other than a number,
#detect their mistake using try and except and print an error message and skip to the next number.
total = 0
count = 0
while True:
    num = input("Enter a number: ")
    if num == 'done':
        print("ALL DONE!")
        break
    else:
        try:
            num = int(num)
            count = count + 1
            total = total + num
        except:
            print("Give me numeric")
            continue
print(total,count,(total/count))
