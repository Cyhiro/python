def calculate_discount(price, discount_percent):
    """
    Calculate the final price after applying a discount.
    If the discount is 20% or higher, apply the discount.
    Otherwise, return the original price.
    """
    if discount_percent >= 20:
        discounted_price = price - (price * discount_percent / 100)
        return discounted_price
    else:
        return price

# Prompt the user for inputs
price = int(input("Enter the original price: "))
discount_percent = float(input("Please enter the discount percentage: "))

# Call the function and calculate the final price
final_price = calculate_discount(price, discount_percent)

# Display the result
if discount_percent >= 20:
    print(f"The price after discount is: {final_price:.2f}")
else:
    print(f"No discount! Price is: {price:.2f}")
