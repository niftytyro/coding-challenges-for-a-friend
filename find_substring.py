# Given two strings, determine if they share a common substring. A substring may be as small as one character.

# Example


# These share the common substring .



# These do not share a substring.

# Function Description

# Complete the function twoStrings in the editor below.

# twoStrings has the following parameter(s):

# string s1: a string
# string s2: another string
# Returns

# string: either YES or NO
# Input Format

# The first line contains a single integer , the number of test cases.

# The following  pairs of lines are as follows:

# The first line contains string .
# The second line contains string .
# Constraints

#  and  consist of characters in the range ascii[a-z].
# Output Format

# For each pair of strings, return YES or NO.

# Sample Input

# 2
# hello
# world
# hi
# world
# Sample Output

# YES
# NO

input_list = []

def twoStrings(s1, s2):
  for i in s1:
    if i in s2:
      return "YES"
  return "NO"

number_of_test_cases = int(input())
for i in range(number_of_test_cases):
  word1 = input()
  word2 = input()
  input_list.append([word1, word2])
for each in input_list:
  print(twoStrings(each[0], each[1]))