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
