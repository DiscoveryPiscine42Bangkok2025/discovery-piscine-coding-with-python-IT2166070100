import sys
print(f"parameters: {len(sys.argv) - 1}")
for param in sys.argv[1:]:
    print(f"{param}: {len(param)}")