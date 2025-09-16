number = int(input("Enter a number less than 25\n"))
if number > 25:
    print("Error")
else:
    while number <= 25:
        print("Inside the loop, my variable", number)
        number += 1