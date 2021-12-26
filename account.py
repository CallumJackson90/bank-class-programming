import json
from pathlib import Path
from random import randint

class Account:
    '''
    A Parent Class defined to contain functions to mimick the operation of
    a standard bank account. To create an Account, an id, balance, and pin
    is required, with balance defaulting to 0 and pin defauling to 1234.
    a_type is used in subclasses to indicate what account type has been
    created.
    
    '''

    def __init__(self, id: int, balance: float = 0, pin: int = 1234, 
                a_type = '', risk = ''):
            '''
            Initialising the class attributes. If an account already exists,
            as shown by an existing {id}.json file, account data is loaded 
            from the file. Otherwise, a new account is created. 
            '''

            assert len(str(id)) == 8, print(f'id number must be 8 digits.')
            assert len(str(pin)) == 4, print(f'pin number must be 4 digits.')
            # Here, we ensure that the id is 8 digits, and the pin is 4.

            if Path(f'{id}.json').is_file():
            # Finds the account file and if it exists, reads from it. 

                with open(f'{id}.json', 'r') as f:
                    accdata = json.load(f)
                    self.id = accdata['id']
                    self.balance = accdata['balance']
                    self.pin = accdata['pin']
                    self.a_type = accdata['type']
                    self.risk = accdata['risk']
        

            else:
                # If the file does not exist, create a new account
                # with the entered id, and generate a random pin.
                self.id = id
                self.balance = balance
                self.pin = randint(1111, 9999)
                self.a_type = a_type
                self.risk = risk
                print(f'Account does not exist, '
                f'creating new account with id: {self.id}.')
                print(f'Account pin set to: {self.pin}.')

            self.save_account()

    def create_account(self):
        '''
        A method to generate an account json file based on current variable
        values for id, balance, pin, and type. Overwrites existing data 
        with new data. file naming format is: '{id}.json'.
        '''

        accdata = {'id' : self.id, 
        'balance' : self.balance,
        'pin' : self.pin,
        'type' : self.a_type,
        'risk' : self.risk}
        with open(f'{self.id}.json', 'w+') as f:
            json.dump(accdata, f)
            f.close()

    def save_account(self):
        '''
        A pointer to the create_account method, called when an account is
        updated and needs to be saved to file.
        '''

        self.create_account()

    def check_pin(self, pin):
        if pin == self.pin:
            correct = True
        else:
            correct = False
        return correct

    def change_pin(self, pins):
        '''
        A method to change the current pin on the account. Requires
        the user to input their old pin before changing to a new one.
        '''
        
        old, new = pins
        if self.check_pin(old):
            self.pin = new
            print(f'Pin changed to: {self.pin}')
        else:
            print('Incorrect Pin.')
        self.save_account()

    def get_balance(self):
        '''
        A simple method to get the current balance of the account.
        '''
        return f'Current balance: £{self.balance}'
        

    def deposit(self, amount, pin):
        '''
        A method to add to the balance, simulating a deposit into
        the account.
        '''
        if not self.check_pin(pin):
            print('Incorrect pin.')
        else:
            self.balance += amount
            self.save_account()
            return f'New balance is: £{self.balance}'

    def __repr__(self):
        '''
        A method to outline how the Account Class is constructed.
        '''
        return f'''{self.__class__.__name__}({self.id}, {self.balance}, 
        {self.pin}'''