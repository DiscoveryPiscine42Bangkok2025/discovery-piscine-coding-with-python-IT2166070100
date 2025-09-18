import sys

if len(sys.argv) != 2:
    print("none")
else:
    text = sys.argv[1]
    count = text.count("z")

    if count > 0:
        print("z" * count)
    else:
        print("none")
