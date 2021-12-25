# bank-class-programming
A simulation of a banking command-line application to practice OOP in Python.

This python mini-project was created to practice creating classes and using inheritance in a python program. 
The general notion of the program is as follows:
* Create a parent class, 'Account', that contains methods required for the basic operation of a 'bank account':
  *  Create a json file, creating a unique id number and assigning a pin and empty balance to new accounts.
  *  Check if such a json file exists, and load it in lieu of creating a new one. 
  *  Methods to allow a user to deposit cash into the account, change their pin number, or check their balance.

* A Subclass, 'CurrentAccount', to build on the functionality of the Account class, predominantly:
  * Adding a method to facilitate withdrawals from the account.

* A second subclass, 'InvestmentAccount', inheriting from 'CurrentAccount' to utilise the withdrawal functionality as well as adding:
  * A method to simulate investing the entirety of an account 'balance' into Low, Medium, and High risk ventures.
    * Low risk ventures result in a change within +/-4% of the initial balance.
    * Medium risk ventures result a change within +/-8% of the initial balance. 
    * High risk ventures result a change within +/-15% of the initial balance.
