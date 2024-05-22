# Simple ATM Program

class ATM:
    def __init__(self):
        self.balance = 0
    
    def check_balance(self):
        print("Your balance is: ₹{:.2f}".format(self.balance))
    
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print("Deposit of ₹{:.2f} successful. Your new balance is: ₹{:.2f}".format(amount, self.balance))
        else:
            print("Invalid amount. Please try again.")
    
    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print("Withdrawal of ₹{:.2f} successful. Your new balance is: ₹{:.2f}".format(amount, self.balance))
        else:
            print("Insufficient funds or invalid amount. Please try again.")

def main():
    atm = ATM()
    pin = "51018"
    attempt = 0
    
    while attempt < 3:
        print("Welcome to Sumit Bank")
        entered_pin = input("Enter pin: ")
        if entered_pin == pin:
            print("\nATM Menu:")
            print("1. Check Balance")
            print("2. Deposit")
            print("3. Withdraw")
            print("4. Exit")
            choice = input("Enter your choice: ")

            if choice == '1':
                atm.check_balance()
            elif choice == '2':
                amount = float(input("Enter amount to deposit: ₹"))
                atm.deposit(amount)
            elif choice == '3':
                amount = float(input("Enter amount to withdraw: ₹"))
                atm.withdraw(amount)
            elif choice == '4':
                print("Thank you for using our ATM. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")
        else:
            attempt += 1
            print("Incorrect PIN. Attempts left:", 3 - attempt)
    
    if attempt == 3:
        print("Too many incorrect attempts. Card blocked. Please contact customer support.")

if __name__ == "__main__":
    main()

# SumitBank = ATM()
# SumitBank.main()
