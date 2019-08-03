# Challenge:
# You are given three inputs: a string, one letter, and a second letter.
# Write a function that returns True if every instance of the first letter 
# occurs before every instance of the second letter.
# Example: first_before_second('a','j','a rabbit jumps joyfully') : output=> True
# Every a comes before j 

# Notes:
# All strings will be in lower case.
# All strings will contain the first and second letters at least once.

# The Brute method
def first_before_second(x,y,sentence):
    found_x = False
    found_y = False
    for s in sentence:
        if s == x:
            if found_y == True:
                # If x has been found after y, return False.
                return False
            # Mark x as having been found, iterate to next character.
            found_x = True
            continue
        if s == y:
            # Found y, check if x has been found yet. If not then return false.
            if found_x == False:
                # x has been found after y, return False.
                return False
            else:
                # found y after x, iterate
                found_y = True
                continue
    # if everything checks out, then safe to return True.
    return True

# The clever method
# If the last instance of x is before the first instance of y
# index of x_n < index of y_1
def first_before_second_2(x,y,sentence):
    return sentence.rindex(x) < sentence.index(y)

print(first_before_second('a','j','a rabbit jumps joyfully'))
print(first_before_second_2('a','j','a rabbit jumps joyfully'))
# True
print(first_before_second("a", "y", "happy birthday"))
print(first_before_second_2("a", "y", "happy birthday"))
# False
print(first_before_second("k", "a","precarious kangaroos"))
print(first_before_second_2("k", "a","precarious kangaroos"))
# False