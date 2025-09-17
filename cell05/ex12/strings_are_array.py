import sys
print("z" * sys.argv[1].count("z") if sys.argv[1].count("z") > 0 and len(sys.argv) == 2 else "none")