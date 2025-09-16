array1 = [2, 8, 9, 48, 8, 22, -12, 2]
print(array1, "\n[", ", ".join(str(i + 2) for i in array1 if i > 5), "]", sep="")
