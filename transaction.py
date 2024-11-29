class Transaction:
  def __init__(self, trans_type, amount, new_balance) -> None:
    self.trans_type = trans_type
    self.amount = amount
    self.new_balance = new_balance
    
  def __str__(self) -> str:
    return f"{self.amount} taka {self.trans_type}. New balance is {self.new_balance}"