'''
Given any number of boolean flags function should return true if and only if one of them is true while others are false.
 If function is called without arguments it should return false.
  only_one() == False
  only_one(True, False, False) == True
  only_one(True, False, False, True) == False
  only_one(False, False, False, False) == False
'''
def only_one(*args):
    if len(args) == 0:
        return False
    nums_of_True = 0
    for arg in args:
        if arg == True:
            nums_of_True += 1
    if nums_of_True == 1:
        return True
    else:
        return False