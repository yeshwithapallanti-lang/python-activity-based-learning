
plans = [
    {
        "name": "Plan A",
        "price": 300,
        "data": 20,
        "calls": 1000,
        "sms": 100,
        "validity": 28,
        "data_rate": 10,
        "call_rate": 0.50,
        "sms_rate": 1.00
    },
    {
        "name": "Plan B",
        "price": 450,
        "data": 40,
        "calls": 1500,
        "sms": 300,
        "validity": 30,
        "data_rate": 8,
        "call_rate": 0.40,
        "sms_rate": 0.50
    },
    {
        "name": "Plan C",
        "price": 250,
        "data": 10,
        "calls": 500,
        "sms": 100,
        "validity": 30,
        "data_rate": 15,
        "call_rate": 0.75,
        "sms_rate": 1.00
    }
]

# User requirements
usage = {
    "data": 30,
    "calls": 800,
    "sms": 120,
    "validity": 28,
    "budget": 500
}

results = []

for plan in plans:
    extra_data = max(0, usage["data"] - plan["data"])
    extra_calls = max(0, usage["calls"] - plan["calls"])
    extra_sms = max(0, usage["sms"] - plan["sms"])

    data_cost = extra_data * plan["data_rate"]
    call_cost = extra_calls * plan["call_rate"]
    sms_cost = extra_sms * plan["sms_rate"]

    total = round(
        plan["price"] + data_cost + call_cost + sms_cost, 2
    )

    eligible = (
        plan["validity"] >= usage["validity"]
        and total <= usage["budget"]
    )

    results.append({
        "name": plan["name"],
        "extra_data": extra_data,
        "extra_calls": extra_calls,
        "extra_sms": extra_sms,
        "total": total,
        "eligible": eligible
    })

# Display all evaluated plans
for result in results:
    print(
        result["name"],
        "| Total: Rs.", result["total"],
        "| Eligible:", result["eligible"]
    )

# Select the cheapest eligible plan
eligible_plans = [
    r for r in results if r["eligible"]
]

if eligible_plans:
    best = min(eligible_plans, key=lambda r: r["total"])
    print("\nRecommended plan:", best["name"])
    print("Estimated cost: Rs.", best["total"])
else:
    print("\nNo plan meets all constraints.")
