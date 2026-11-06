import product

# A
b = product.Product("banana", 0.25)
m = product.Merch("mug", 20, "Aron")
if b.__lt__(m):
  print(b.get_name() + " is less than " + m.get_name())

# B
# b = product.Product("banana", 0.25)
# m = product.Merch("mug", 20, "Aron")
# if b < m:
#   print(b.get_name + " is less than " + m.get_name)

# C
# b = product.Product("banana", 0.25)
# m = product.Merch("mug", 20, "Aron")
# if b < m:
#   print(b.get_name() + " is less than " + m.get_name())

# D. None of the above

# E. More than one of the above**