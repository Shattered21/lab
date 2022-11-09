

class Account:

    def __init__(self, name: str) -> None:

        self.__account_name = name  # Name of the account
        self.__account_balance = 0.00  # Balance of the account

    def deposit(self, amount: float) -> bool:
        """
        Method that increase account balance
        :param amount: amount the user wants to deposit into account
        """
        if amount <= 0:
            return False
        else:
            self.__account_balance + amount
            return True

    def withdraw(self, amount: float) -> bool:
        '''
        Method that reduces the amount of account balance
        :param amount: amount user wants to take out of account balance
        '''
        if (amount <= 0) or (amount < self.__account_balance):
            return False
        else:
            self.__account_balance - amount
            return True

    def get_balance(self) -> float:
        '''
        Method to get account balance
        :returns: account balance
        '''
        return self.__account_balance


    def get_name(self) -> str:
        '''
        Method to get account name
        :returns: account name
        '''
        return self.__account_name  # Returns the name of the account




