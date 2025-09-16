age = int(input("Please tell me your age: "))
print(f"You are currently {age} years old.", *[f"\nIn {i} years, you'll be {age+i} years old." for i in [10,20,30]])
