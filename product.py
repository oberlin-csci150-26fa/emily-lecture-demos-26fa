class Product:
	quantity = 0 # class variable

	def __init__(self, n, p):
		self.name = n 					# name as string 
		self.price = float(p) 	# dollars as float
		Product.quantity += 1 # updates class variable

	def get_name(self):
		return self.name

	def get_price(self):
		return self.price

	def get_product_quantity(self):
		return Product.quantity

	def set_price(self, new_p):
		self.price = new_p
		return

	def __lt__(self, other_product):
		if self.price < other_product.price:
			return True
		else:
			return False
		
	def __gt__(self, other_product):
		if self.price > other_product.price:
			return True
		else:
			return False

class Merch(Product): 
  def __init__(self, n, p, m): 
    super().__init__(n, p)
    self.maker = m # name of maker as string



