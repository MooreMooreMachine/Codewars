# Given a string of integers, return the number of odd-numbered substrings that can be formed.
#
# For example, in the case of "1341", they are 1, 1, 3, 13, 41, 341, 1341, a total of 7 numbers.
#
# solve("1341") = 7. See test cases for more examples.
#
# Good luck!
#
# If you like substring Katas, please try


def solve(s):
    def combine_by_digit(string, width):
        position = 0
        while position <= len(string) - width:
            if int(string[position:position + width]) % 2 != 0:
               yield string[position:position + width]
            position += 1
    result = 0
    for num in range(1, len(s) + 1):
        result += len(list(combine_by_digit(s, num)))
    return result





