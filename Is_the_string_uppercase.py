'''
Is the string uppercase?
Task

Create a method to see whether the string is ALL CAPS.
Examples (input -> output)

"c" -> False
"C" -> True
"hello I AM DONALD" -> False
"HELLO I AM DONALD" -> True
"ACSKLDFJSgSKLDFJSKLDFJ" -> False
"ACSKLDFJSGSKLDFJSKLDFJ" -> True

In this Kata, a string is said to be in ALL CAPS whenever it does not contain any lowercase letter so any string containing no letters at all is trivially considered to be in ALL CAPS.
'''

def is_uppercase(inp):
    special_characters = "\"!@#$%^&*()-+?_=,<>/\""
    if all(c in special_characters for c in inp):
        return True
    return(True if inp.isupper() else False)

print(is_uppercase('I AM DONAL'))
print(is_uppercase('asdI AM DONAL'))
print(is_uppercase('!@#$I AM DONAL'))
print(is_uppercase('!@#$'))
