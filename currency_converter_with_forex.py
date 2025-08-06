from forex_python.converter import CurrencyRates

c = CurrencyRates()
amount = float(input("Enter the amount for conversion : "))
conversion_from = input("What currency do you want to convert from? : ").upper()
conversion_to = input("What currency do you want to convert to? : ").upper()

converted = c.convert(conversion_from, conversion_to, amount)

print(f"{amount} {conversion_from} = {converted} {conversion_to}")
