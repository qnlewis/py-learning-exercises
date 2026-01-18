import uuid


class SameAccount(Exception):
    pass


class DifferentBanks(Exception):
    pass


class InsufficientFunds(Exception):
    pass


class Account:
    def __init__(self, bank, id, balance=0):
        self.bank = bank
        self.id = id
        self._balance = balance

    @property
    def balance(self):
        return self._balance

    def __eq__(self, other):
        return (
            isinstance(other, self.__class__)
            and self.bank == other.bank
            and self.id == other.id
        )


class Bank:
    def __init__(self):
        self.accounts = {}
        self.transfer_log = []

    def create_account(self, balance=0):
        account_id = str(uuid.uuid4())
        account = Account(self, account_id, balance)
        self.accounts[account_id] = account
        return account

    def transfer(self, from_account, to_account, amount):
        if from_account == to_account:
            raise SameAccount("Cannot transfer to the same account")

        if from_account.bank != to_account.bank:
            raise DifferentBanks("Cannot transfer between different banks")

        if from_account.balance < amount:
            raise InsufficientFunds("Insufficient funds for transfer")

        from_account._balance -= amount
        to_account._balance += amount

        self.transfer_log.append((from_account, to_account, amount))