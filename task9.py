
# Multi-Currency Travel Budget Analysis System

# Illustrative exchange rates: INR per unit of currency
exchange_rates = {
    "EUR": 100.00,
    "USD": 85.00,
    "GBP": 110.00
}

# Each expense contains a category, currency and amount
expenses = [
    {"category": "Accommodation", "currency": "EUR", "amount": 300},
    {"category": "Food", "currency": "EUR", "amount": 120},
    {"category": "Transport", "currency": "USD", "amount": 80},
    {"category": "Shopping", "currency": "GBP", "amount": 100},
    {"category": "Sightseeing", "currency": "USD", "amount": 50}
]

budget = 70000.00
fee_rate = 0.02

category_totals = {}
total_converted = 0.0
total_fees = 0.0

print("\n======= TRAVEL EXPENSE REPORT =======")
print(f"{'Category':<16} {'Converted':>12} {'Fee':>10} {'Total':>12}")

for expense in expenses:
    currency = expense["currency"]
    amount = expense["amount"]

    if currency not in exchange_rates:
        raise ValueError(f"Missing exchange rate: {currency}")

    if amount < 0:
        raise ValueError("Expense amount cannot be negative.")

    converted = amount * exchange_rates[currency]
    fee = converted * fee_rate
    total = converted + fee

    total_converted += converted
    total_fees += fee

    category = expense["category"]
    category_totals[category] = (
        category_totals.get(category, 0) + total
    )

    print(
        f"{category:<16} "
        f"Rs.{converted:>9.2f} "
        f"Rs.{fee:>7.2f} "
        f"Rs.{total:>9.2f}"
    )

total_spending = total_converted + total_fees
balance = budget - total_spending

print("--------------------------------------")
print(f"Converted expenses: Rs.{total_converted:.2f}")
print(f"Conversion fees:    Rs.{total_fees:.2f}")
print(f"Total spending:     Rs.{total_spending:.2f}")
print(f"Travel budget:      Rs.{budget:.2f}")

if total_spending <= budget:
    print(f"Status: WITHIN BUDGET")
    print(f"Remaining: Rs.{balance:.2f}")
else:
    print("Status: OVER BUDGET")
    print(f"Excess: Rs.{abs(balance):.2f}")

if category_totals:
    largest_category = max(
        category_totals,
        key=category_totals.get
    )
    print(f"Largest category: {largest_category}")
    print(
        f"Category total: "
        f"Rs.{category_totals[largest_category]:.2f}"
    )

print("======================================")
