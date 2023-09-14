class BankAccount:

  def __init__(self,
               account_number,
               account_name,
               account_holder_name,
               initial_balance=0):
    self._account_number = account_number
    self._account_name = account_name
    self._account_holder_name = account_holder_name
    self._account_balance = initial_balance

  def deposit(self, amount):
    if amount > 0:
      self._account_balance += amount
      return f"Deposited ${amount}. New balance: ${self._account_balance}"
    else:
      return "Invalid deposit amount. Please enter a positive value."

  def withdraw(self, amount):
    if amount > 0 and amount <= self._account_balance:
      self._account_balance -= amount
      return f"Withdrew ${amount}. New balance: ${self._account_balance}"
    elif amount <= 0:
      return "Invalid withdrawal amount. Please enter a positive value."
    else:
      return "Insufficient funds for withdrawal."

  def display_balance(self):
    return f"Account balance for {self._account_holder_name}: ${self._account_balance}"


# Create an instance of the BankAccount class
account1 = BankAccount("123456789", "Savings", "John Doe", 1000)

# Test deposit functionality
print(account1.deposit(500))  # Deposited $500. New balance: $1500

# Test withdrawal functionality
print(account1.withdraw(200))  # Withdrew $200. New balance: $1300
print(account1.withdraw(1500))  # Insufficient funds for withdrawal.

# Display account balance
print(account1.display_balance())  # Account balance for John Doe: $1300
