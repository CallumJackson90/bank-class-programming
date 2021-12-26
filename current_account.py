from account import Account
import json

class CurrentAccount(Account):
    '''
    A subclass created from the superclass Account, enabling withdrawals.
    The separation of withdrawal and deposit between the classes is designed
    to accomodate for future developments of the BussinessAccount, which will
    not have direct withdrawls.
    '''
    def __init__(self, id: int, balance: float = 0, pin: int = 1234, 
                a_type ='C', risk = ''):
        super().__init__(
            id,
            balance,
            pin
        )
        self.a_type = a_type
        super().save_account()
    
    def withdraw(self, amount, pin):
        '''
        A method to subtract a given amount from balance, 
        simulating a withdrawal.
        '''
        if not super().check_pin(pin):
            print('Incorrect pin.')
        else:
            self.balance -= amount
            super().save_account()
            return f'New balance is: £{self.balance}'

