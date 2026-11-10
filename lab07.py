
print("=" * 40)
print("     CALENDAR VERIFICATION SYSTEM")
print("=" * 40)

year = int(input("Enter year: "))

print()

if year <= 0:
    print("Error: Invalid Year")
else:
    if year % 400 == 0:
        status = "LEAP YEAR"
        reason = "Century year divisible by 400"
    elif year % 100 == 0:
        status = "COMMON YEAR"
        reason = "Century year not divisible by 400"
    elif year % 4 == 0:
        status = "LEAP YEAR"
        reason = "Divisible by 4 and not a century year"
    else:
        status = "COMMON YEAR"
        reason = "Not divisible by 4"

    if status == "LEAP YEAR":
        feb_days = 29
        total_days = 366
    else:
        feb_days = 28
        total_days = 365

    print("-" * 40)
    print("Year:", year)
    print("Status:", status)
    print("Days in Year:", total_days, "days")
    print("Days in February:", feb_days, "days")
    print("Reason:", reason)
    print("-" * 40)
