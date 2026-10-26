
# Manufacturing Cost and Profitability Analysis

# Production details
units_produced = 500
units_sold = 500
selling_price = 150
target_profit = 18000

# Manufacturing costs (illustrative)
material_cost = 40000
wastage_cost = 2000
labour_cost = 10000
machine_cost = 5000
overhead_cost = 3000

# Validate production quantities
if units_produced <= 0:
    raise ValueError("Units produced must be positive.")

if units_sold < 0 or units_sold > units_produced:
    raise ValueError("Units sold must be between 0 and units produced.")

if selling_price < 0 or target_profit < 0:
    raise ValueError("Price and target profit cannot be negative.")

# Calculate total production cost
total_cost = (
    material_cost
    + wastage_cost
    + labour_cost
    + machine_cost
    + overhead_cost
)

cost_per_unit = total_cost / units_produced

# Assume all batch costs are incurred for this analysis.
revenue = units_sold * selling_price
profit = revenue - total_cost

profit_margin = (
    (profit / revenue) * 100
    if revenue > 0 else 0
)

required_price = (
    (total_cost + target_profit) / units_sold
    if units_sold > 0 else None
)

# Display report
print("\n=== MANUFACTURING PROFIT REPORT ===")
print(f"Units produced:       {units_produced}")
print(f"Units sold:           {units_sold}")
print(f"Material cost:        Rs.{material_cost:.2f}")
print(f"Wastage cost:         Rs.{wastage_cost:.2f}")
print(f"Labour cost:          Rs.{labour_cost:.2f}")
print(f"Machine cost:         Rs.{machine_cost:.2f}")
print(f"Factory overhead:     Rs.{overhead_cost:.2f}")
print(f"Total production cost: Rs.{total_cost:.2f}")
print(f"Cost per unit:         Rs.{cost_per_unit:.2f}")
print(f"Sales revenue:         Rs.{revenue:.2f}")
print(f"Profit:                Rs.{profit:.2f}")
print(f"Profit margin:         {profit_margin:.2f}%")
print(f"Target profit:         Rs.{target_profit:.2f}")

if profit >= target_profit:
    print("Status: PROFIT TARGET ACHIEVED")
else:
    shortfall = target_profit - profit
    print("Status: PROFIT TARGET NOT ACHIEVED")
    print(f"Profit shortfall: Rs.{shortfall:.2f}")

if required_price is not None:
    print(f"Required selling price per unit: "
          f"Rs.{required_price:.2f}")

print("====================================")
