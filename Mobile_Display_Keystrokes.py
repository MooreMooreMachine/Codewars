# Given a string, return the number of keystrokes necessary to type it. You can assume
# that the input will entirely consist of characters included in the mobile layout (lowercase letters, digits, and the symbols * and #).
# Examples
#
# "*#"       =>  2 (1 + 1)
# "123"      =>  3 (1 + 1 + 1)
# "abc"      =>  9 (2 + 3 + 4)
# "codewars" => 26 (4 + 4 + 2 + 3 + 2 + 2 + 4 + 5)

def mobile_keyboard(s):
    keys = {'1':'1234567890*#', '2':'adgjmptw', '3':'behknqux', '4':'cfilorvy','5':'sz'}
    sum_of_keystrokes = 0
    for symbol in s:
        if symbol in keys['1']:
            sum_of_keystrokes += 1
        elif symbol in keys['2']:
            sum_of_keystrokes += 2
        elif symbol in keys['3']:
            sum_of_keystrokes += 3
        elif symbol in keys['4']:
            sum_of_keystrokes += 4
        elif symbol in keys['5']:
            sum_of_keystrokes += 5
    return sum_of_keystrokes

print(mobile_keyboard('longwordwhichdontreallymakessense'))