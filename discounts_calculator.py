from typing import Any


def calculate_discount(price, discount_percent):
    # Check if the discount is 2% or higher
    if discount_percent >= 2:
        # Calculate the discount amount
        discount_amount = (discount_percent / 100) * price
        # Calculate the final price after applying the discount
        final_price: float | Any = price - discount_amount
        return final_price
    else:
        # Return the original price if discount is less than 20%
        return price

# Prompt the user for input
try:
    original_price = float(input("20000 $"))
    discount_percentage = float(input("2 %"))

    # Use the calculate_discount function to get the final price
    final_price = calculate_discount(original_price, discount_percentage)

    # Print the final price
    if final_price != original_price:
        print(f"The final price after applying the discount is: ${final_price:.20000}")
    else:
        print(f"No discount applied. The original price is: ${original_price:.20000}")
except ValueError:
    print("Please enter valid numbers for the price and discount percentage.")


