
def allocate_scholarships(students, slots):
    eligible = []
    rejected = []

    for student in students:
        reasons = []

        if student["aggregate"] < 75:
            reasons.append("Aggregate below 75%")

        if min(student["subjects"]) < 60:
            reasons.append("Subject marks below 60%")

        if student["attendance"] < 80:
            reasons.append("Attendance below 80%")

        if student["income"] > 250000:
            reasons.append("Income exceeds limit")

        if reasons:
            rejected.append({
                "name": student["name"],
                "reasons": reasons
            })
        else:
            eligible.append(student)

    # Apply the university's published ranking rules.
    eligible.sort(
        key=lambda s: (
            -s["aggregate"],
            -s["core_subject"],
            -s["attendance"],
            s["income"],
            s["tie_lottery_number"]
        )
    )

    selected = eligible[:slots]

    return {
        "selected": selected,
        "eligible_waitlist": eligible[slots:],
        "rejected": rejected
    }
