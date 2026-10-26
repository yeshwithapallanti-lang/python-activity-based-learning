
def progressive_deduction(gross):
    slabs = [
        (20000, 0.00),
        (15000, 0.05),
        (15000, 0.10),
        (float("inf"), 0.15)
    ]

    remaining = gross
    deduction = 0

    for limit, rate in slabs:
        amount = min(remaining, limit)
        deduction += amount * rate
        remaining -= amount

        if remaining <= 0:
            break

    return round(deduction, 2)


def calculate_payroll(
    employee_id,
    name,
    basic,
    allowances,
    overtime,
    incentives,
    pf,
    insurance
):
    earnings = [basic, allowances, overtime, incentives]
    other_deductions = [pf, insurance]

    if any(x < 0 for x in earnings + other_deductions):
        raise ValueError("Amounts cannot be negative")

    gross = sum(earnings)

    progressive = progressive_deduction(gross)
    total_deductions = progressive + pf + insurance
    net = gross - total_deductions

    if net < 0:
        raise ValueError("Net salary cannot be negative")

    return {
        "Employee ID": employee_id,
        "Employee Name": name,
        "Basic Pay": basic,
        "Allowances": allowances,
        "Overtime": overtime,
        "Incentives": incentives,
        "Gross Salary": gross,
        "Progressive Deduction": progressive,
        "Provident Fund": pf,
        "Insurance": insurance,
        "Total Deductions": total_deductions,
        "Net Salary": round(net, 2)
    }


statement = calculate_payroll(
    "EMP101", "Rahul Kumar",
    30000, 11000, 2000, 2000,
    1800, 300
)

for item, amount in statement.items():
    if isinstance(amount, (int, float)):
        print(f"{item}: Rs. {amount:,.2f}")
    else:
        print(f"{item}: {amount}")
