# # # # # # # # # # # # # # 
# The challenge
# Semantic Versions
# You're fed up about changing the version of your software manually. Instead, you will create a
# little script that will make it for you.
# Create a function nextVersion, that will take a string in parameter,
# and will return a string containing the next version number.
#
# Rules
# No number but the first may be greater than 9: if any are, you must set them to 0 
# and increment the next number in sequence.
# You can assume all tests inputs to be valid.
# # # # # # # # # # # # # # 

import unittest

class TestChallenge(unittest.TestCase):
    def test_simple_case(self):
        self.assertEqual(nextVersion("1.2.3"), "1.2.4")
        
    def test_new_subversion_case(self):
        self.assertEqual(nextVersion("1.2.3.9"), "1.2.4.0")
        
    def test_nines_case(self):
        self.assertEqual(nextVersion("9.9.9.9"), "10.0.0.0")

def nextVersion(current_version: str) -> str:
    # Strategy:
    # Break up the number by dot
    # Loop through the array in reverse order, incrementing it by 1 then taking the left most number.
    # Maintain the other number as "remainder" if it exists
    # Add the remainder to the next number
    # Join the array and return as string, adding remainder if it exists to the left of the number (all nines case)
    current_version_array = reversed(current_version.split("."))
    new_version = []
    remainder = 1
    for i in current_version_array:
        new_number, remainder = increment(int(i), remainder)
        new_version.append(str(new_number))
    result = '.'.join(reversed(new_version))
    return str(remainder) + result if remainder else result

def increment(number: int, remainder: int) -> tuple[int, int]:
    number += remainder
    number_str = str(number)
    return int(number_str[-1]), int(number_str[0]) if len(number_str) > 1 else 0

if __name__ == '__main__': 
    unittest.main() 