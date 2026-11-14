"""
Program Design

Example:
rev("hello") --> "olleh"
rev("racecar") --> "racecar"

# 1. What should be the base case?
One character string "s" "s"
Empty string "" ""

# 2. How do we make the problem smaller?
Process each letter
Decrease length of string each time
input = "hello"
         "ello"
input[1:]

input = "hello"
        "hell"
input[:-1]

#  3. How do we combine the solutions to the smaller problems to get the overall solution?
input <-- "hello"
return input[-1] + input[:-1]
       "o".      + "hell"

return input[-1] + rev(input[:-1])

"""

def rev(w):
  """ recursive function for reversing a string """
  # base case
  if len(w) == 0:
    return ""
  # not base case
  #reverse of everything else + # first letter put at the end
  return rev(w[1:]) + w[0]

print(rev("racecar"))
print(rev("nascar"))
print(rev("flugelhorn"))