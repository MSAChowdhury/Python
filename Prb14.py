#Write another program that prompts for a list of numbers as above and at the end prints out both the maximum and minimum of the numbers.
total = 0
count = 0
max = 0
min = None
while True:
    num = input("Enter a number: ")
    if num == 'done':
        print("ALL DONE!")
        break
    else:
        try:
            num = int(num)
            if max < num:
                max = num
            if min == None or min > num:
                min = num
            count = count + 1
            total = total + num
        except:
            print("Give me numeric")
            continue
print(total,count,max,min)
