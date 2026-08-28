from datetime import datetime


DAY_NAMES = {
    'Monday': 'Monday',
    'Tuesday': 'Tuesday',
    'Wednesday': 'Wednesday',
    'Thursday': 'Thursday',
    'Friday': 'Friday',
    'Saturday': 'Saturday',
    'Sunday': 'Sunday',
}


def format_datetime(dt):
    day_name = DAY_NAMES[dt.strftime('%A')]
    month_name = dt.strftime('%B')
    day = dt.day
    year = dt.year

    hour_12 = dt.hour % 12
    if hour_12 == 0:
        hour_12 = 12
    am_pm = 'am' if dt.hour < 12 else 'pm'
    time_str = f"{hour_12}:{dt.minute:02d}{am_pm}"

    return f"{day_name}, {month_name} {day}, {year}, at {time_str}"


class BankAccount:
    def __init__(self, owner_name=""):
        self.owner_name = owner_name
        self.balance = 0

    def deposit(self, amount):
        if amount <= 0:
            print("Deposit amount must be greater than zero")
            return

        self.balance += amount
        now = datetime.now()
        print(f"{amount} SAR has been deposited to your account on {format_datetime(now)}.")

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be greater than zero")
            return

        if amount > self.balance:
            print("Sorry, your balance is insufficient for this withdrawal")
            return

        self.balance -= amount
        now = datetime.now()
        print(f"{amount} SAR has been withdrawn from your account on {format_datetime(now)}.")

    def get_balance(self):
        return self.balance


if __name__ == "__main__":
    account = BankAccount("Khalid")

    account.deposit(2000)
    account.withdraw(150)

    print(f"\nYour current balance is: {account.get_balance()} SAR")

    account.withdraw(100000)