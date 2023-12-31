# In this kata you need to build a function to return either true/True or false/False
# if a string can be seen as the repetition of a simpler/shorter subpattern or not.
#
# For example:
#
# has_subpattern("a") == False #no repeated pattern
# has_subpattern("aaaa") == True #created repeating "a"
# has_subpattern("abcd") == False #no repeated pattern
# has_subpattern("abababab") == True #created repeating "ab"
# has_subpattern("ababababa") == False #cannot be entirely reproduced repeating a pattern
#
# Strings will never be empty and can be composed of any character
# (just consider upper- and lowercase letters as different entities)
# and can be pretty long (keep an eye on performances!).
#
# If you liked it, go for the next kata of the series!


def has_subpattern(strng):
    for step in range(1, int(len(strng) / 2) + 1):
        sublist = []
        for i in range(0, len(strng), step):
            sublist.append(strng[i:i + step])
        if len(set(sublist)) == 1:
            return True
    return False

print(has_subpattern('abbaabbaabba'))

