
def distance_fare(distance):
    if distance <= 0:
        raise ValueError("Distance must be positive")

    fare = 0

    first = min(distance, 100)
    fare += first * 1.00

    second = min(max(distance - 100, 0), 200)
    fare += second * 0.80

    remaining = max(distance - 300, 0)
    fare += remaining * 0.60

    return fare


CLASS_MULTIPLIERS = {
    "Sleeper": 1.0,
    "AC 3-Tier": 1.8,
    "AC 2-Tier": 2.5,
    "AC First Class": 3.5
}


def age_concession(age):
    if age < 0:
        raise ValueError("Age cannot be negative")
    if age < 5:
        return 1.00
    elif age < 12:
        return 0.50
    elif age >= 60:
        return 0.10
    return 0.00


def calculate_passenger_fare(
    age, distance, travel_class,
    reservation_fee=40
):
    if travel_class not in CLASS_MULTIPLIERS:
        raise ValueError("Invalid travel class")

    if reservation_fee < 0:
        raise ValueError("Reservation fee cannot be negative")

    base = distance_fare(distance)
    class_fare = base * CLASS_MULTIPLIERS[travel_class]

    concession_rate = age_concession(age)
    discount = class_fare * concession_rate

    final_fare = round(
        class_fare - discount + reservation_fee, 2
    )

    return {
        "base_fare": round(base, 2),
        "class_fare": round(class_fare, 2),
        "concession": round(discount, 2),
        "reservation_fee": reservation_fee,
        "total": final_fare
    }


def cancellation_refund(amount_paid, hours_before):
    if amount_paid < 0 or hours_before < 0:
        raise ValueError("Invalid cancellation details")

    if hours_before > 48:
        penalty = 100
    elif hours_before >= 12:
        penalty = amount_paid * 0.25
    else:
        penalty = amount_paid * 0.50

    penalty = min(amount_paid, penalty)

    return {
        "penalty": round(penalty, 2),
        "refund": round(amount_paid - penalty, 2)
    }


# Example booking with multiple passengers
passengers = [
    {"name": "Passenger A", "age": 35},
    {"name": "Passenger B", "age": 65}
]

booking_total = 20  # One booking service fee

for passenger in passengers:
    result = calculate_passenger_fare(
        passenger["age"], 350, "AC 3-Tier"
    )
    passenger["fare"] = result["total"]
    booking_total += result["total"]

    print(passenger["name"], result)

print("Total booking cost:", round(booking_total, 2))

# Example cancellation for one passenger
refund = cancellation_refund(
    passengers[0]["fare"], 24
)
print("Cancellation:", refund)
