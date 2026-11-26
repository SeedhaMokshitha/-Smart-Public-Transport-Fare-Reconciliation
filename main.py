# Smart Public Transport Fare Reconciliation

def calculate_fare(base_fare, adults, students, seniors):
    adult_fare = base_fare
    student_fare = base_fare * 0.80   # 20% discount
    senior_fare = base_fare * 0.90    # 10% discount

    total = (adults * adult_fare +
             students * student_fare +
             seniors * senior_fare)

    return total


def main():
    routes = []
    total_expected = 0
    total_collected = 0

    n = int(input("Enter number of routes: "))

    for i in range(n):
        print("\nRoute", i + 1)

        route_name = input("Enter route name: ")
        base_fare = float(input("Enter base fare: "))

        adults = int(input("Enter adult passengers: "))
        students = int(input("Enter student passengers: "))
        seniors = int(input("Enter senior passengers: "))

        actual = float(input("Enter actual revenue collected: "))

        expected = calculate_fare(
            base_fare, adults, students, seniors
        )

        discrepancy = actual - expected

        routes.append({
            "route": route_name,
            "expected": expected,
            "actual": actual,
            "discrepancy": discrepancy
        })

        total_expected += expected
        total_collected += actual

    print("\n========== FARE RECONCILIATION ==========")

    for route in routes:
        print("\nRoute:", route["route"])
        print("Expected Revenue: Rs.", round(route["expected"], 2))
        print("Actual Revenue: Rs.", round(route["actual"], 2))
        print("Discrepancy: Rs.", round(route["discrepancy"], 2))

        if route["discrepancy"] < 0:
            print("Status: Revenue Shortage")
        elif route["discrepancy"] > 0:
            print("Status: Extra Revenue")
        else:
            print("Status: Revenue Matched")

    total_discrepancy = total_collected - total_expected

    print("\n========== OVERALL SUMMARY ==========")
    print("Total Expected Revenue: Rs.", round(total_expected, 2))
    print("Total Collected Revenue: Rs.", round(total_collected, 2))
    print("Total Discrepancy: Rs.", round(total_discrepancy, 2))

    if total_discrepancy < 0:
        print("Overall Status: Revenue Shortage")
    elif total_discrepancy > 0:
        print("Overall Status: Extra Revenue")
    else:
        print("Overall Status: Revenue Matched")


if __name__ == "__main__":
    main()
