amount_purchase = float(input("Enter the amount of a purchase: "))
state_tax = amount_purchase * .05
county_tax = amount_purchase * 0.025
total_sale_tax = state_tax + county_tax
total_sale = amount_purchase + total_sale_tax

print(f"The amount of purchase: {amount_purchase}, state sales tax: {state_tax},\n"
      f"Country sales tax: {county_tax}, Total sales tax: {total_sale_tax},\n"
      f"Total of the sale: {total_sale}")
