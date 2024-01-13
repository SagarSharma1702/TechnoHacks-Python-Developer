'''Task 6 : ATM simulator
Create a program that simulates the all atm
functionalities and operations (Check balance,
Deposit, Withdraw)'''
class ATM:
  def __init__(self, balance=0):
      self.balance = balance

  def check_balance(self):
      return f"Your balance is ${self.balance:.2f}"

  def deposit(self, amount):
      if amount > 0:
          self.balance += amount
          return f"${amount:.2f} deposited successfully. Your new balance is ${self.balance:.2f}"
      else:
          return "Invalid deposit amount. Please enter a positive number."

  def withdraw(self, amount):
      if amount > 0 and amount <= self.balance:
          self.balance -= amount
          return f"${amount:.2f} withdrawn successfully. Your new balance is ${self.balance:.2f}"
      elif amount <= 0:
          return "Invalid withdrawal amount. Please enter a positive number."
      else:
          return "Insufficient funds. Withdrawal amount exceeds your balance."

def atm_simulator():
  print("Welcome to the ATM Simulator!")
  initial_balance = float(input("Enter your initial balance: $"))
  atm = ATM(initial_balance)

  while True:
      print("\n1. Check Balance")
      print("2. Deposit")
      print("3. Withdraw")
      print("4. Exit")

      choice = input("Enter your choice (1-4): ")

      if choice == '1':
          print(atm.check_balance())
      elif choice == '2':
          amount = float(input("Enter the deposit amount: $"))
          print(atm.deposit(amount))
      elif choice == '3':
          amount = float(input("Enter the withdrawal amount: $"))
          print(atm.withdraw(amount))
      elif choice == '4':
          print("Thank you for using the ATM Simulator. Have a great day!")
          break
      else:
          print("Invalid choice. Please enter a number between 1 and 4.")

# Call the atm_simulator function to start the ATM simulation
atm_simulator()
