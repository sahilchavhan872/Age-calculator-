from datetime import date

def calculate_age(birth_date):
    today = date.today()
    age_years = today.year - birth_date.year
    age_months = today.month - birth_date.month
    age_days = today.day - birth_date.day

    if age_days < 0:
        age_months -= 1
        age_days += 30

    if age_months < 0:
        age_years -= 1
        age_months += 12

    return age_years, age_months, age_days

dob_input = input("Enter your date of birth (YYYY-MM-DD): ")
dob_parts = [int(part) for part in dob_input.split('-')]
dob = date(dob_parts[0], dob_parts[1], dob_parts[2])

years, months, days = calculate_age(dob)
print(f"Your age is {years} years, {months} months, and {days} days.")