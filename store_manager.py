import product

b = product.Product("banana", 0.25)
m1 = product.Merch("mug", 20, "Aron")
m2 = product.Merch("mug", 20, "Amanda")

print(product.Product.quantity)
print(b.get_product_quantity())