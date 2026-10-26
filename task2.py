
def calculate_energy(units):
    if units < 0:
        raise ValueError("Units cannot be negative")

    rates = [
        (100, 2),
        (100, 3),
        (300, 5)
    ]

    energy = 0
    remaining = units

    for limit, rate in rates:
        slab_units = min(remaining, limit)
        energy += slab_units * rate
        remaining -= slab_units

        if remaining <= 0:
            break

    if remaining > 0:
        energy += remaining * 7

    return energy


def calculate_bill(units, eligible_for_rebate=True):
    energy = calculate_energy(units)
    fixed_charge = 100
    surcharge = energy * 0.05

    rebate = energy * 0.10 if eligible_for_rebate else 0

    total = energy + fixed_charge + surcharge - rebate

    return round(total, 2)


def compare_months(previous_units, current_units):
    if previous_units <= 0:
        return "Insufficient previous usage for comparison"

    increase = (
        (current_units - previous_units)
        / previous_units
    ) * 100

    if increase > 30:
        return f"Alert: Usage increased by {increase:.1f}%"

    return f"Usage change: {increase:.1f}%"
