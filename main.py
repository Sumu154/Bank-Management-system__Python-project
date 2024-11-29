from bank import Bank 
from user import AccountHoler, Admin  



def main():
  bank = Bank('Sumaiya_Ltd.')
  admin = Admin("Bank Manager")

  while True:
    print("\n=== Welcome to Bank Management System ===")
    print("1. Admin Panel")
    print("2. Account Holder Panel")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        admin_panel(bank, admin)
    elif choice == "2":
        account_holder_panel(bank)
    elif choice == "3":
        print("Thank you for using the Bank Management System!")
        break
    else:
        print("Invalid choice. Please try again.")



def admin_panel(bank, admin):
  while True:
    print("\n=== Admin Panel ===")
    print("1. Create Account")
    print("2. Delete Account")
    print("3. View All Accounts")
    print("4. Check Total Available Balance")
    print("5. Check Total Loan Amount")
    print("6. Toggle Loan Feature")
    print("7. Back to Main Menu")

    choice = input("Enter your choice: ")

    if choice == "1":
      name = input("Enter account holder's name: ")
      phone = input("Enter phone number: ")
      email = input("Enter email: ")
      address = input("Enter address: ")
      acc_type = input("Enter account type (savings/current): ")
      admin.create_account(bank, name, phone, email, address, acc_type)
    elif choice == "2":
      account_id = int(input("Enter account ID to delete: "))
      admin.delete_account(bank, account_id)
    elif choice == "3":
      admin.view_all_accounts(bank)
    elif choice == "4":
      admin.total_available_balance(bank)
    elif choice == "5":
      admin.total_loan_amount(bank)
    elif choice == "6":
      admin.toggle_loan_feature()
    elif choice == "7":
      break
    else:
      print("Invalid choice. Please try again.")



def account_holder_panel(bank):
  account_id = int(input("Enter your Account ID: "))
  account = bank.accountHolders.get(account_id)

  if not account:
    print("Account not found.")
    return

  while True:
    print("\n=== Account Holder Panel ===")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Get Loan")
    print("5. Transfer Money")
    print("6. View Transaction History")
    print("7. Back to Main Menu")

    choice = input("Enter your choice: ")

    if choice == "1":
      print(f"Your current balance is: {account.get_balance()}")
    elif choice == "2":
      amount = float(input("Enter deposit amount: "))
      account.deposit_balance(amount)
    elif choice == "3":
      amount = float(input("Enter withdrawal amount: "))
      account.withdraw_balance(amount)
    elif choice == "4":
      if bank.loan_feature_on:
        loan = float(input("Enter loan amount: "))
        account.get_loan(loan)
      else:
        print("Loan feature is currently turned off.")
    elif choice == "5":
      receiver_id = int(input("Enter recipient's Account ID: "))
      amount = float(input("Enter transfer amount: "))
      bank.transfer_amount(account.account_id, receiver_id, amount)
    elif choice == "6":
      print("\nTransaction History:")
      for it in account.trans_history:
        print(it)
    elif choice == "7":
      break
    else:
      print("Invalid choice. Please try again.")



if __name__ == "__main__":
  main()
