'''Task 2 : Currency Converter
Build a program that can convert currency
from one form to another using the latest
exchange rates.'''
#Step 1 : pip install forex-python
from forex_python.converter import CurrencyRates

def convert_currency(amount, from_currency, to_currency):
    c = CurrencyRates()

    try:
        exchange_rate = c.get_rate(from_currency, to_currency)
        converted_amount = amount * exchange_rate
        return converted_amount
    except:
        return "Error: Unable to fetch exchange rates."

def currency_converter():
    try:
        amount = float(input("Enter the amount: "))
        from_currency = input("Enter the source currency code (e.g., USD): ").upper()
        to_currency = input("Enter the target currency code (e.g., EUR): ").upper()

        result = convert_currency(amount, from_currency, to_currency)
        print(f"{amount} {from_currency} is equal to {result:.2f} {to_currency}")

    except ValueError:
        print("Invalid input. Please enter a valid number.")

# Call the currency_converter function
currency_converter()
