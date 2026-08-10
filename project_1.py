phone_book = {
    "1111111111": "Amal",
    "2222222222": "Mohammed",
    "3333333333": "Khadijah",
    "4444444444": "Abdullah",
    "5555555555": "Rawan",
    "6666666666": "Faisal",
    "7777777777": "Layla"
}
def is_valid_number(number):
    count = 0
    for char in number:
        count += 1
    if count != 10:
        return False
    for char in number:
        if char < '0' or char > '9':
            return False
    return True

def find_name_by_number():
    phone_number = input("Enter the phone number: ")
    if is_valid_number(phone_number):
        for number in phone_book:
            if phone_number == number:
                print(phone_book[phone_number])
                return
        print("Sorry, the number is not found")
    else:
        print("This is invalid number")

def find_number_by_name():
    name = input("Enter the name:")
    for number, owner in phone_book.items():
        if owner == name:
            print(number)
            return
    print("Sorry, the name is not found")

def add_new_contact():
    new_name = input("Add new name:")
    new_number = input("Add new number:")
    if is_valid_number(new_number):
        phone_book[new_number] = new_name
        print("Contact added successfully!")
    else:
        print("This is invalid number")

def main():
    while True:
        print("\n1. Find name by number")
        print("2. Find number by name")
        print("3. Add new contact")
        print("4. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            find_name_by_number()
        elif choice == "2":
            find_number_by_name()
        elif choice == "3":
            add_new_contact()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, please try again")

if __name__ == "__main__":
    main()