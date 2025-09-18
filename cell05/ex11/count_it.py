import sys
if len(sys.argv) >= 2:
    print(f"parameters: {len(sys.argv) - 1}")
    for param in sys.argv[1:]:
        print(f"{param}: {len(param)}")
else:
    print("none")