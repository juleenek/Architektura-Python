import pytest

from bankaccount import BankAccount, InvalidAmountError

# Testy dla klasy BankAccount

def test_initial_balance():
    account = BankAccount(100)
    assert account.get_balance() == 100

def test_deposit():
    account = BankAccount()
    account.deposit(50)
    assert account.get_balance() == 50

def test_withdraw():
    account = BankAccount(100)
    account.withdraw(50)
    assert account.get_balance() == 50

def test_insufficient_funds():
    account = BankAccount(100)
    with pytest.raises(InvalidAmountError, match="Insufficient funds."):
        account.withdraw(200)

def test_deposit_negative_amount():
    account = BankAccount()
    with pytest.raises(InvalidAmountError, match="Amount to deposit must be positive and greater than zero."):
        account.deposit(-50)

def test_withdraw_negative_amount():
    account = BankAccount(100)
    with pytest.raises(InvalidAmountError, match="Amount to withdraw must be positive and greater than zero."):
        account.withdraw(-50)
