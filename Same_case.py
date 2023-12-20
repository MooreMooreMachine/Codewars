def same_case(a: str, b: str):
    if a.isupper() and b.isupper() or a.islower() and b.islower():
        return 1
    elif a.isupper() and b.islower() or a.islower() and b.isupper():
        return 0
    else:
        return -1