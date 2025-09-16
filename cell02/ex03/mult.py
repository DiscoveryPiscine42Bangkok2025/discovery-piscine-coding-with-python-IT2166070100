first = int(input("Enter the first number: \n"))
second = int(input("Enter the second number: \n"))
ans = first * second
print(first, "x", second , f" = {ans}")
if ans == 0:
    print("The result is a positive and negative.")
elif ans > 0:
    print("The result is positive.")
else:
    print("The result is negative.")