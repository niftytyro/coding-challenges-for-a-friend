# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets. Open brackets must be closed in the correct order.

# Input Format

# First line of input contains string s

# Constraints

# 1 <= s.length <= 104
# s consists of parentheses only '()[]{}'.
# Output Format

# Print 1 if valid else print 0.

# Sample Input 0

# ()
# Sample Output 0

# 1
# Sample Input 1

# ()[]{}
# Sample Output 1

# 1
# Sample Input 2

# (]
# Sample Output 2

# 0
opening_braces = ["(", "[", "{"]
closing_braces = [")", "]", "}"]
braces_order = []

input_string = input()

isValid = True

for each in input_string:
  if each in opening_braces: 
    braces_order.append(opening_braces.index(each))
  elif each in closing_braces:
    if closing_braces.index(each) == braces_order[-1]:
      del braces_order[-1]
    else:
      isValid = False
      break

if isValid:
  print(1)
else:
  print(0)
