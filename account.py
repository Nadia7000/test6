
class Account:
   """
​
   """

   def __init__(self, account_id, account_pin, balance=0):
       self.account_id = account_id
       self.account_pin = account_pin
       self.balance = balance

   def get_account_id(self):
       """
​
       :return:
       """
       return self.account_id

   def get_account_balance(self):
       """
​
       :return:
       """
       return self.balance

   def withdraw_from_account(self, amount):
       """
​
       :param amount:
       :return:
       """

       self.balance -= amount

   def deposit_to_account(self, amount):
       """
       Method for depositing money to the account
       :param amount: amount to deposit
       Note: Updating account balance
       """
       self.balance += amount

