"""
Pydantic is the most widely used data validation library for Python.
It lets you structure your data, gives you type-hints and auto-complete in your IDE,
and helps to serialize to and from JSON
"""

from pydantic import BaseModel, field_validator, SecretStr, Field

from rich import traceback

traceback.install()

class Account(BaseModel, validate_assignment=True):
    name: str = Field(..., min_length=3, max_length=50)
    password: SecretStr
    balance: float

    @field_validator("balance")
    def balance_must_be_positive(cls, value):
        if value < 0:
            raise ValueError("balance must be positive")
        else:
            return value

if __name__ == "__main__":

    account = Account(name="John", password="password", balance=100)

    account.balance = 100
    account.name = "Humphrey"
    print(account)