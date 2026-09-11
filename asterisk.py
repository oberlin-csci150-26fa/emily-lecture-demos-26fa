"""
Given: 
n total rows
r for the current row
We're printing asterisks and spaces

Loop ingredients?
Variable: r 
Sequence: (1, n+1)
Body: use formulas to concatenate/print asterisks and spaces

"""

n = 5
for r in range(1, n+1):
  print( (n-r)*' ' + (2*r-1)*'*' + (n-r)*' ')