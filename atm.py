from account import Account
from random import randint


def atm_actions(account=None, retries=3, account_ids=[]):
   """
​
   :param account:
   :param retries:
   :param account_ids:
   :return:
   """
   session_actions = 15
   account_id = int(input('\nPlease enter account id: '))
   if account_id == 0:
       new_account_id = randint(1, 1000)
       new_account_pin = int(input('\nPlease enter new pin (4 digit): '))
       new_account = Account(account_id=new_account_id, account_pin=new_account_pin)
       account_ids.append(new_account_id)
       print(f'\nYour account had been created with id: {new_account_id}')
       atm_actions(account=new_account, account_ids=account_ids)
   elif account.account_id in account_ids:
       for tries in range(session_actions):
           if tries == (session_actions - 1):
               print('\nYou used 3 attempts, please access our atm again')
               exit()
           current_account_pin = int(input('\nPlease enter your pin: '))
           if current_account_pin != account.account_pin:
               atm_actions(account=account, account_ids=account_ids, retries=retries - 1)
           print('\n1 - View Balance \t 2 - Withdraw \t 3 - Deposit\t 4 - Exit')
           user_selection = int(input('\nEnter your selection: '))
           if user_selection == 1:
               print(f'\nCurrent account balance is: {account.get_account_balance()}')
               continue
           elif user_selection == 2:
               to_withdraw = int(input('\nPlease enter amount to withdraw: '))
               if (account.get_account_balance() - to_withdraw) < 0:
                   print('\nThis account doesn\'t have enough money on the balance')
                   continue
               else:
                   account.withdraw_from_account(amount=to_withdraw)
                   continue
           elif user_selection == 3:
               to_deposit = int(input('\nPlease enter amount to deposit: '))
               verify_amount_to_deposit = input('\nIs this correct amount to deposit? Yes, or No? ')
               if verify_amount_to_deposit == 'Yes':
                   account.deposit_to_account(amount=to_deposit)
               else:
                   continue
           elif user_selection == 4:
               print('\nTransaction complete')
               print(f'\nTransaction number: {randint(10000, 1000000)}')
               print('\nThank you for using out ATM')
               exit()
           else:
               print('\nThat\'s invalid choice ')
   else:
       print(f'\nWrong account id please retry, you have {retries} more attempts')
       atm_actions(account=account, account_ids=account_ids, retries=retries - 1)

