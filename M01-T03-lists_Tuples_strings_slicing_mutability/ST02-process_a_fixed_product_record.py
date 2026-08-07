product_id = input()
product_name = input()
category = input()
unit_price = float(input())
quantity = int(input())
reorder_level = int(input())

# Create the fixed product record as a tuple
product_tuple = (product_id, product_name, category, unit_price, quantity)

# Access the product ID and product name using indexes
p_id = product_tuple[0]
p_name = product_tuple[1]

# Unpack the complete tuple
prod_id, prod_name, category, unit_price, quantity = product_tuple

# Calculate the stock value
stock_value = unit_price * quantity

# Determine the stock status
if quantity == 0:
    stock_status = "Out of Stock"
elif quantity <= reorder_level:
    stock_status = "Reorder Required"
else:
    stock_status = "Sufficient Stock"

# Display the complete processed product record
print(f"Product ID: {prod_id}")
print(f"Product Name: {prod_name}")
print(f"Category: {category}")
print(f"Unit Price: {unit_price:.2f}")
print(f"Available Quantity: {quantity}")
print(f"Stock Value: {stock_value:.2f}")
print(f"Stock Status: {stock_status}")