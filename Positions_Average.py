
#Example:
# Given string s = "444996, 699990, 666690, 096904, 600644, 640646, 606469, 409694, 666094, 606490"
# composing a set of n = 10 substrings (hence 45 combinations), pos_average returns 29.2592592593.

def pos_average(s):
    list_of_strings = s.split(', ')
    sum_of_position = len(list_of_strings) * len(list_of_strings[0])
    same_value = 0
    def compere_by_position_func(s1:str, s2:str):
        compare_count = 0
        for index_pos in range(len(s1)):
            if s1[index_pos] == s2[index_pos]:
                compare_count += 1
        return compare_count
    for print_head in range(len(list_of_strings)):
        for other in list_of_strings[print_head + 1:]:
            same_value += compere_by_position_func(list_of_strings[print_head], other)
    return (same_value / sum_of_position) * 100
print(pos_average("466960, 069060, 494940, 060069"))
# 12 --> 3   466960
# 13 --> 3   069060
# 14 --> 2   494940
# 23 --> 1   060069
# 24 --> 4
# 34 --> 0

#  sum len = 24 compare = 13 % = 54
