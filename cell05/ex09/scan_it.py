import sys, re
if len(sys.argv) != 3:
    print("none")
else:
    matches = re.findall(sys.argv[1], sys.argv[2])
    print(len(matches) if matches else "none")
