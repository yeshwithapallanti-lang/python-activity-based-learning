
def generate_bill(
    patient_id,
    consultation,
    diagnostics,
    treatment,
    concession_rate,
    amount_paid
):
    # Validate inputs
    if not patient_id:
        raise ValueError("Patient ID is required")

    charges = [consultation, diagnostics, treatment]

    if any(charge < 0 for charge in charges):
        raise ValueError("Charges cannot be negative")

    if not 0 <= concession_rate <= 100:
        raise ValueError("Invalid concession percentage")

    gross_bill = sum(charges)
    concession = round(
        gross_bill * concession_rate / 100, 2
    )
    final_bill = round(gross_bill - concession, 2)

    if amount_paid < 0:
        raise ValueError("Payment cannot be negative")

    if amount_paid > final_bill:
        raise ValueError("Payment exceeds outstanding bill")

    balance = round(final_bill - amount_paid, 2)

    if balance == 0:
        status = "Fully paid"
    elif amount_paid > 0:
        status = "Partially paid"
    else:
        status = "Unpaid"

    return {
        "patient_id": patient_id,
        "gross_bill": gross_bill,
        "concession": concession,
        "final_bill": final_bill,
        "amount_paid": amount_paid,
        "balance_due": balance,
        "payment_status": status
    }


bill = generate_bill(
    patient_id="P101",
    consultation=500,
    diagnostics=1500,
    treatment=5000,
    concession_rate=10,
    amount_paid=6300
)

for key, value in bill.items():
    print(f"{key}: {value}")
