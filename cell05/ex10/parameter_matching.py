import sys 
if len(sys.argv) == 2:
    text = str(input("What was the paremeter? "))
    print("Good job!" if sys.argv[1] == text else "Nope, sorry...")
else:
    print("none")