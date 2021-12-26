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


* In the main program, an interface is provided to the user, allowing them to access these functions, as well as:
  * Provide a way to convert a Current Account into an Investment Account.
  * If the balance of an Investment Account falls below the threshold (>£10,000), the account is downgraded to a Current Account.


Below are some screenshots of the working code to highlight particular areas of the program. 

![image](https://user-images.githubusercontent.com/74067072/147395334-5c901525-f260-4805-97ca-65c3afda5211.png)



This image shows account generation, after entering an id that did not exist, the program created a new Account, and provided us with a random pin.
It also highlghts the menu presented to the user after getting their Account set up.

![image](https://user-images.githubusercontent.com/74067072/147395370-a0c00f21-be8e-40fb-a5e1-8e19612f0532.png)

Here, we use an existing account and no new generation occurs.

![image](https://user-images.githubusercontent.com/74067072/147395421-2f8aa457-bbef-4d1f-bbd7-74d080246619.png)

We then proceed to deposit £10,000 (Out of thin air, wouldn't that be nice!), and here we can see the balance updating.

![image](https://user-images.githubusercontent.com/74067072/147395455-43ce3994-cf77-44ee-90e6-db294615dd20.png)

And, withdrawing money works in largely the same manner.

![image](https://user-images.githubusercontent.com/74067072/147395488-36936d86-5db9-4d42-860a-219b033d0228.png)

Changing our pin is rather straightforward.

Below, we take a look at some of the features for an 'Investment Account'.

![image](https://user-images.githubusercontent.com/74067072/147395516-a35c0cae-0ee9-4de7-9ab5-8dfc1d8a0b03.png)

As our balance is over £10,000, we qualify for an 'Investment Account.



We increase our risk tolerance, in the hopes of increasing returns from the simulated market.



