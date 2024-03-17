# Step 1: Define the function calculate_discount with two parameters: price and discount_percent
def calculate_discount(price, discount_percent):
    
    # Step 2: Check if the discount_percent is 20% or higher
    if discount_percent >= 20:
        
        # Step 3: Calculate the discount amount
        discount_amount = price * (discount_percent / 100)
        
        # Step 4: Calculate the final price after applying the discount
        final_price = price - discount_amount
        
        # Step 5: Return the final price
        return final_price
    
    # Step 6: If the discount is less than 20%, return the original price
    else:
        return price
    # Example usage:
original_price = 100
discount_percentage = 25
final_price = calculate_discount(original_price, discount_percentage)
#print("Final price after discount:", final_price)
def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        return final_price
    else:
        return price
    
    

# Prompt the user to enter the original price and discount percentage
original_price = float(input("Enter the original price of the item: "))
discount_percentage = float(input("Enter the discount percentage: "))

# Calculate the final price using the calculate_discount function
final_price = calculate_discount(original_price, discount_percentage)

# Print the final price after applying the discount, or the original price if no discount was applied
if final_price == original_price:
    print("No discount applied. Final price:", original_price)
else:
    print("Final price after discount:", final_price)

