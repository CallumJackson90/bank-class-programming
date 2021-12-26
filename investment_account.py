from current_account import CurrentAccount
import json
from random import uniform


class InvestmentAccount(CurrentAccount):
    '''
    A Subclass of CurrentAccount, inheriting the withdrawal functionality
    whilst building its own functions to simulate an investment account.
    This class comes with a new attribute, risk, allowing a user to choose
    how much risk to expose their investment account to.  
    '''
    def __init__(self, id: int, balance: float = 0, pin: int = 1234, 
            risk = 'L', a_type = 'I'):
        super().__init__(
            id,
            balance,
            pin,
        )
        assert isinstance(risk, (str)), f'''Risk must be: \
                            'L', 'M', or 'H', got {risk}'''
        # This ensures the entered risk falls into one of three categories.
        self.risk = risk
        self.a_type = a_type
        super().save_account()

    def investment_returns(self):
        '''
        A method to simulate investment returns. The function generates a 
        random float respective of risk level, and adjusts the balance 
        according to this. For the sake of simplicity, it is assumed the
        investment is applied to the whole balance, and the returns are 
        generated and collected when the user checks. 
        '''
        if self.risk == 'L':
            pc_change = round(uniform(-0.04, 0.04), 4)
        elif self.risk == 'M':
            pc_change = round(uniform(-0.08, 0.08), 4)
        else:
            pc_change = round(uniform(-0.15, 0.15), 4)

        print(f'Returns for this period were: {pc_change*100} percent.')
        self.balance = round(self.balance * (1.0 + pc_change), 2)
        super().save_account()
        return super().get_balance()

    def update_risk(self, risk):
        '''
        A small function to update the risk exposure of an investment
        account and update the account file.
        '''
        self.risk = risk
        super().save_account()
    