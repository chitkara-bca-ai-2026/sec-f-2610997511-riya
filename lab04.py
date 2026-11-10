print("==============================================================")
print("====================DATA CONVERSION UTILITY===================")
print("==============================================================")

name = input("Enter product name: ")
price = float(input("Enter product price: "))
quantity = int(input("Enter product quantity: "))

total = price * quantity
amount = str(total)

print("Product name    :", name)
print("Product price   :", price)
print("Product quantity:", quantity)

print("--------------------------------------------------------------")
print("                        TYPE CASTING                          ")
print("--------------------------------------------------------------")
print("VARIABLE               VALUE                    PYTHON TYPE")
print("--------------------------------------------------------------")
print("name                   ", name, "                    ", type(name))
print("price                  ", price, "                    ", type(price))
print("quantity               ", quantity, "                    ",    type(quantity))
print("total                  ", total, "                    ", type(total))
print("amount                 ", amount, "                    ", type(amount))
print("--------------------------------------------------------------")

print("--------------------------------------------------------------")
print("                        TAX CONVERSION                        ")
print("--------------------------------------------------------------")

print("Product name     :", name)
print("Price per unit   :", price)
print("Quantity         :", quantity)
print("--------------------------------------------------------------")
print("Invoice Total    :", total)

print("==============================================================")
