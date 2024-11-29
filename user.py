from abc import ABC    # abstract base class
from transaction import Transaction
from bank import Bank


class User(ABC):
  def __init__(self, name, phone, email, address) -> None:
    self.name = name
    self.phone = phone
    self.email = email
    self.address = address


class AccountHoler(User):
  _id = 1

  def __init__(self, name, phone, email, address, acc_type) -> None:
    super().__init__(name, phone, email, address)
    self.acc_type = acc_type
    self.balance = 0
    self.account_id = AccountHoler._id  # Assign the current _id to account_id
    AccountHoler._id += 1  # Increment the class-level _id
    self.getLoanTimes = 0
    self.bank = Bank('b1')
    self.trans_history = []
    self.loan_amounts = []
    
    

  def get_balance(self):
    return self.balance

  def withdraw_balance(self, withdraw):
    if self.bank.isBankrupt:  # Access the bank's isBankrupt attribute through self.bank
      print("The bank is bankrupt.")
      return
    if withdraw > self.balance:  # Check if withdrawal amount exceeds balance
      print("Withdrawal amount exceeded")
      return
    elif withdraw <= 0:  # Check if the withdrawal amount is negative or zero
      print("Withdrawal amount must be positive")
      return
    self.balance -= withdraw  # Deduct the withdrawal amount from balance
    transaction = Transaction('Withdraw', withdraw, self.balance)
    self.trans_history.append(transaction)
    print("Withdraw balance successfully!!")


  def deposit_balance(self, deposit):
    if deposit<0:
      print("deposit amount must ne positive")
      return
    self.balance += deposit
    transaction = Transaction('deposit', deposit, self.balance)
    self.trans_history.append(transaction)
    print("deposit balance successfully!!")

  def get_loan(self, loan):
    if not self.bank.loan_feature_on:  # Check if loan feature is ON in the bank
      print("Loan feature is currently disabled by the bank.")
      return
    if self.getLoanTimes >= 2:
      print("You have already received a loan two times!")
      return
    
    self.balance += loan  
    self.getLoanTimes += 1 
    self.loan_amounts.append(loan)
    transaction = Transaction('Loan', loan, self.balance)
    self.trans_history.append(transaction)
    print(f"You have received a loan of {loan} successfully!")




class Admin:
  def __init__(self, name):
    self.name = name
    self.loan_feature_on = True

  def create_account(self, bank_name, name, phone, email, address, acc_type):
    account = AccountHoler(name, phone, email, address, acc_type)
    bank_name.add_account(account)
    print(f"Account created for {name} with ID {account.account_id}")

  def delete_account(self, bank_name, account_id):
    if account_id in bank_name.accountHolders:
      del bank_name.accountHolders[account_id]
      print(f"Account with ID {account_id} has been deleted.")
    else:
      print(f"No account found with ID {account_id}.")

  def view_all_accounts(self, bank_name):
    print("All Accounts:")
    if len(bank_name.accountHolders) == 0:
      print("No user to show!")
      return
    print("ID\tName\t\tBalance")
    for it in bank_name.accountHolders.values():
      print(f"{it.account_id}\t{it.name}\t\t{it.balance}")

  def total_available_balance(self, bank_name):
    total_balance = sum(account.balance for account in bank_name.accountHolders.values())
    print(f"Available balance: {total_balance}")
    return total_balance

  def total_loan_amount(self, bank_name):
    total_loan = sum(sum(account.loan_amounts) for account in bank_name.accountHolders.values())
    print(f"Total loan amount given by {bank_name.name}: {total_loan}")
    return total_loan

  def toggle_loan_feature(self):
    self.loan_feature_on = not self.loan_feature_on
    state = "ON" if self.loan_feature_on else "OFF"
    print(f"Loan feature is now {state}.")


  
# ac1 = AccountHoler('Sumaiya', 121212, 'sumaiya@gmail.com', 'Dhaka', 'savings' )
# ac1.deposit_balance(2000)
# ac1.get_loan(3000)
# print(ac1.balance)


    

  

   
    