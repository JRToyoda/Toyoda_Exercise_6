i = 0
total = 0
num = input("Enter a number or press Enter to quit: ")

if num == "":
    quit()

else:

    while num:
        i += 1
        total += float(num)
        num = input("Enter a number or press Enter to quit: ")

    print("The sum is", total, "\nThe average is", total / i)
