from datetime import date
import calendar


class InvalidDateError(Exception):
    pass


def parse_date(date_str):
    parts = date_str.strip().split('-')
    if len(parts) != 3:
        raise InvalidDateError

    try:
        day, month, year = (int(p) for p in parts)
    except ValueError:
    
        raise InvalidDateError


    if day < 0 or month < 0 or year < 0:
        raise InvalidDateError

    if not (1 <= month <= 12):
        raise InvalidDateError

    if year < 1:
        raise InvalidDateError

    max_day = calendar.monthrange(year, month)[1]
    if not (1 <= day <= max_day):
        raise InvalidDateError

    try:
        return date(year, month, day)
    except ValueError:
        raise InvalidDateError


def calculate_age(birth_date, today=None):

    today = today or date.today()
    age = today.year - birth_date.year
    if (today.month, today.day) < (birth_date.month, birth_date.day):
        age -= 1
    return age


def main():
    people = []  

    print("enter the name and date of birth in the format: Name, dd-mm-yyyy")
    print("leave the line empty to finish input\n")

    while True:
        line = input().strip()
        if line == "":
            break

        if ',' not in line:
            print("Invalid input format. Please use the format: Name, dd-mm-yyyy")
            continue

        name_part, date_part = line.split(',', 1)
        name = name_part.strip()

        try:
            birth_date = parse_date(date_part)
        except InvalidDateError:
            print(f"Invalid date - {name}")
            continue

        age = calculate_age(birth_date)
        day_name = birth_date.strftime('%A')

        people.append({
            'name': name,
            'birth_date': birth_date,
            'age': age,
            'day_name': day_name,
        })

    if not people:
        print("No valid data entered.")
        return

    print()
    for p in people:
        print(f"{p['name']} is {p['age']} years old and she/he was born on {p['day_name']}")

    if len(people) == 1:
        print("There is no oldest or youngest person")
    else:
        oldest = max(people, key=lambda p: p['age'])
        youngest = min(people, key=lambda p: p['age'])
        print(f"The oldest one is {oldest['name']}")
        print(f"The youngest one is {youngest['name']}")

    print(f"Total People: {len(people)}")

   
    print("\n-- younger to older --")
    sorted_people = sorted(people, key=lambda p: p['age'], reverse=True)
    for p in sorted_people:
        print(f"{p['name']} ({p['age']})")

   
    print("\n-- inputs in reverse order --")
    for p in reversed(people):
        print(f"{p['name']}, {p['birth_date'].strftime('%d-%m-%Y')}")

   
    print("\n-- born on sunday --")
    sunday_people = [p['name'] for p in people if p['day_name'] == 'Sunday']
    if sunday_people:
        for name in sunday_people:
            print(name)
    else:
        print("No people were born on Sunday")


if __name__ == "__main__":
    main()