def shrink(s = None):
    if len(s) >= 8:
        return s[0:8]
    else:
        return s
    
def enlarge(s = None):
    if len(s) < 8:
        return s + "*" * (8 - len(s))
    else:
        return s