from account import Account
from current_account import CurrentAccount
from investment_account import InvestmentAccount
import json
from pathlib import Path

menu_return = 'Press enter to continue: '

def check_account(acc_num):
    if Path(f'{acc_num}.json').is_file():
    # Finds the account file and if it exists, reads from it. 
        with open(f'{acc_num}.json', 'r') as f:
            accdata = json.load(f)
            data = (accdata['type'], accdata['balance'], 
            accdata['pin'], accdata['risk'])
    else:
        data = None
    return data

def main():
    '''
    The main program. Here, the user is presented with a command-line
    interface to interact with their account. A user can check their 
    balance, deposit, withdraw (Current and Investment accounts only),
    and Investment accounts can check returns on investments.
    
    '''
    acc_num = input('Enter your account number:')
    accdata = check_account(acc_num)
    if accdata is not None:
        if accdata[0] == 'I':
            # If the account is an investment account, construct the
            # data using the InvestmentAccount class.
            current_account = InvestmentAccount(acc_num, accdata[1], 
                                accdata[2], accdata[3])
        elif accdata[0] == 'C':
            # If the account is a Current account, construct the
            # data using the CurrentAccount class.
            current_account = CurrentAccount(acc_num, accdata[1], 
                                accdata[2])
    else:
        # If the account does not exist, create a new one.
        current_account = CurrentAccount(acc_num)

    finished = False


    if current_account != None:
        # Ensure the account is created before entering the main loop.
        while not finished:
            if (current_account.balance < 10000 and 
            current_account.a_type == 'I'):
            # If a user's balance falls below the £10000 minimumn 
            # required to have an investment account, 'reconstruct' 
            # the account to be a standard Current account.
                current_account = CurrentAccount(acc_num, a_type='C')
                print('Unfortunately, you have fallen below our '
                'minimumn balance threshhold for Investment accounts.')
                print('We have converted your account to a Current Account.')
                input(menu_return)

            # Present the user with a menu of options.
            to_do = input(f'''
            Hello customer {current_account.id}, what would you like to do?
            Account type: {current_account.__class__.__name__}.
            C: Check balance
            D: Deposit
            W: Withdraw
            P: Change Pin
            I: Apply for Investment Account
            SR: Set Risk (Investment Account only)
            CR: Check Investment returns (Investment Account only)
            B: Apply for Business Account
            Q: Quit
            
            Please enter an option: ''')
            
            # Conditional logic to determine what class method to access.
            if to_do == 'Q':
                finished = True
                print('Thank you for banking with us!')

            elif to_do == 'C':
                print(current_account.get_balance())
                input(menu_return)

            elif to_do == 'D':
                pin = int(input('Please enter your pin: '))
                amount = float(input('Please enter the deposit amount: '))
                print(current_account.deposit(amount, pin))
                input(menu_return)

            elif to_do == 'W':
                pin = int(input('Please enter your pin: '))
                amount = float(input('Please enter the withdrawal amount: '))
                print(current_account.withdraw(amount, pin))
                input(menu_return)

            elif to_do == 'P':
                old = int(input('Please enter your current pin: '))
                new = int(input('Please enter the new pin you would like: '))
                pins = old, new
                current_account.change_pin(pins)
                input(menu_return)

            elif to_do == 'I':
                if current_account.balance < 10000:
                    print('Sorry, you must have £10000 in your account to '
                        'invest.')
                    input(menu_return)

                else:
                    print('Congratulations! you qualify '
                        'for an investment account. '
                        '\nRisk tolerance has been set to a default of L. '
                        'To change this, please see the corresponding '
                        '\nmenu entry.')
                        
                    id = current_account.id
                    balance = current_account.balance
                    pin = current_account.pin
                    current_account = InvestmentAccount(id, balance, pin)
                    input(menu_return)


            elif to_do == 'SR':
                if current_account.a_type == 'I':
                    print(f'Current risk level: {current_account.risk}')
                    risk = input('''Available risk levels:
                    L: Low risk: +/-4 percent returns
                    M: Medium risk: +/- 8 percent returns
                    H: High risk: +/-15 percent returns
                    Please enter a risk level: ''')

                    print(f'Risk set to: {risk}.')
                    current_account.update_risk(risk)
                    input(menu_return)
                else:
                    print('Setting risk is only applicable '
                    'to Investment Accounts.')
                    input(menu_return)


            elif to_do == 'CR':
                if (current_account.__class__.__name__ 
                            != 'InvestmentAccount'):
                    print('Sorry, you must have an Investment ' 
                        'account for this.')
                    input(menu_return)
                else:
                    print('Checking investment returns...')
                    print(current_account.investment_returns())
                    input(menu_return)

            elif to_do == 'B':
                print('We are working to expand our account offerings. '
                'Please check back soon!')
                input(menu_return)

            else:
                print('Invalid input.')
                input(menu_return)


if __name__ == '__main__':
    main()
    
