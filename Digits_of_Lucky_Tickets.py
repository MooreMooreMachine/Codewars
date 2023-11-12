# Create a function that calculates the count of n-digit strings with the same sum for the first half and second half of their digits. These digits are referred to as "lucky" digits.
#
# Examples
#
# Input: 2 ➞ Output: 10
# # "00", "11", "22", "33", "44", "55", "66", "77", "88", "99"
#
# Input: 4 ➞ Output: 670
#
# Input: 6 ➞ Output: 55252
# # "000000", "001010", "112220", ..., "999999"


def lucky_ticket(n):
    dict = {}
    max_digit =  int(n/2) * '9'
    for n in range(int(max_digit) + 1):
        current_sum = 0
        for dig in str(n):
            current_sum += int(dig)
        if str(current_sum) not in dict.keys():
            dict.setdefault(str(current_sum), 1)
        else:
            dict[str(current_sum)] += 1
    return sum(dict.values())

print(lucky_ticket(4))
