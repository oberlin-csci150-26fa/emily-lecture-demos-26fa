import product

class Merch(product.Product): 
  def __init__(self, n, p, m): 
    super().__init__(n, p)
    self.maker = m # name of maker as string

# Discuss: Make test instances of product
# Tea

# Ceramics
c = Merch("mug", 20.0, "Sam")
print(c.get_price())
print(c.price)

# Fruit

# Cookie