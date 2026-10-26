
import math

# Campus Event Financial Planning System

# Fixed event costs (illustrative)
venue_cost = 12000
equipment_cost = 8000
transport_cost = 5000

# Variable costs per participant
catering_per_person = 180
certificate_per_person = 20

# Funding and registration settings
expected_participants = 100
sponsorship = 20000
registration_fee = 300

# Calculate fixed and variable costs
fixed_cost = venue_cost + equipment_cost + transport_cost
variable_cost_per_person = (
    catering_per_person + certificate_per_person
)

expected_variable_cost = (
    expected_participants * variable_cost_per_person
)

total_cost = fixed_cost + expected_variable_cost
funding_shortfall = max(0, total_cost - sponsorship)

# Required contribution if the expected number registers
if expected_participants > 0:
    contribution_needed = (
        funding_shortfall / expected_participants
    )
else:
    contribution_needed = 0

# Break-even calculation
remaining_fixed_cost = max(0, fixed_cost - sponsorship)
contribution_margin = (
    registration_fee - variable_cost_per_person
)

if remaining_fixed_cost == 0:
    break_even_registrations = 0
elif contribution_margin > 0:
    break_even_registrations = math.ceil(
        remaining_fixed_cost / contribution_margin
    )
else:
    break_even_registrations = None

# Display report
print("\n=== CAMPUS EVENT FINANCIAL REPORT ===")
print(f"Venue cost:              Rs.{venue_cost:.2f}")
print(f"Equipment cost:          Rs.{equipment_cost:.2f}")
print(f"Transport cost:          Rs.{transport_cost:.2f}")
print(f"Fixed cost:              Rs.{fixed_cost:.2f}")
print(f"Variable cost/person:   Rs.{variable_cost_per_person:.2f}")
print(f"Expected variable cost: Rs.{expected_variable_cost:.2f}")
print(f"Total event cost:        Rs.{total_cost:.2f}")
print(f"Confirmed sponsorship:  Rs.{sponsorship:.2f}")
print(f"Funding shortfall:       Rs.{funding_shortfall:.2f}")
print(f"Contribution needed:    Rs.{contribution_needed:.2f}")
print(f"Registration fee:       Rs.{registration_fee:.2f}")

if break_even_registrations is None:
    print("Break-even: Not possible at this fee.")
    print("Increase the fee or reduce costs.")
else:
    print(
        f"Minimum break-even registrations: "
        f"{break_even_registrations}"
    )

# Check expected participation
if break_even_registrations is not None:
    if expected_participants >= break_even_registrations:
        print("Expected attendance can cover costs.")
    else:
        print("Expected attendance is below break-even.")

print("======================================")
