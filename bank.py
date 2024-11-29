from transaction import Transaction
from user import User, AccountHoler, Admin

class Bank:
  _id = 1

  def __init__(self, name) -> None:
      self.name = name
      Bank._id += 1
      self.loan_feature_on = True
      self.accountHolders = {}

  def add_account(self, account):
      self.accountHolders[account.account_id] = account

  def transfer_amount(self, sender_id, receiver_id, amount):
      sender = self.accountHolders.get(sender_id)
      receiver = self.accountHolders.get(receiver_id)

      if not sender:
          print("Sender account does not exist.")
          return
      if not receiver:
          print("Receiver account does not exist.")
          return
      if amount <= 0:
          print("Transfer amount must be positive")
          return
      if amount > sender.balance:
          print("Insufficient balance in sender's account.")
          return

      # Perform the transfer
      sender.balance -= amount
      receiver.balance += amount

      # Log transactions
      sender_transaction = Transaction('Transfer out', amount, sender.balance)
      receiver_transaction = Transaction('Transfer in', amount, receiver.balance)
      sender.trans_history.append(sender_transaction)
      receiver.trans_history.append(receiver_transaction)
      print(f"Successfully transferred {amount} from {sender_id} to {receiver_id}.")
