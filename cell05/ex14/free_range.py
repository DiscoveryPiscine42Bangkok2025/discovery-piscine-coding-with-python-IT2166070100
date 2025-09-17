import sys
array = [i for i in range(int(sys.argv[1]), int(sys.argv[2]) + 1)]
print("[" + ", ".join(str(i) for i in array) + "]")