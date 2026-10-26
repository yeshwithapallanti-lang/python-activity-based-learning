
# Retail Billing System with Multiple Discount Rules

products = [
    {"name": "Rice", "category": "grocery",
     "price": 60, "quantity": 2},
    {"name": "Shirt", "category": "apparel",
     "price": 800, "quantity": 1},
    {"name": "Bag", "category": "accessories",
     "price": 500, "quantity": 1}
]

# Illustrative tax configuration
tax_rates = {
    "grocery": 0.05,
    "apparel": 0.12,
    "accessories": 0.18
}

discount_threshold = 1200
discount_rate = 0.10
maximum_discount = 150

subtotal = sum(
    item["price"] * item["quantity"]
    for item in products
)

# Apply threshold discount and concession limit
if subtotal >= discount_threshold:
    discount = min(
        subtotal * discount_rate,
        maximum_discount
    )
else:
    discount = 0

# Allocate the discount proportionally
total_tax = 0

print("\n========== RETAIL INVOICE ==========")
print(f"{'Product':<12} {'Qty':>3} {'Amount':>10} {'Tax':>10}")

for item in products:
    amount = item["price"] * item["quantity"]

    # Proportional allocation of bill discount
    item_discount = discount * amount / subtotal
    discounted_amount = amount - item_discount

    rate = tax_rates[item["category"]]
    item_tax = discounted_amount * rate
    total_tax += item_tax

    print(
        f"{item['name']:<12} "
        f"{item['quantity']:>3} "
        f"₹{discounted_amount:>8.2f} "
        f"₹{item_tax:>8.2f}"
    )

final_bill = subtotal - discount + total_tax

print("------------------------------------")
print(f"Subtotal:       ₹{subtotal:.2f}")
print(f"Discount:      -₹{discount:.2f}")
print(f"Total Tax:      ₹{total_tax:.2f}")
print(f"FINAL BILL:     ₹{final_bill:.2f}")
print("====================================")
