import httpx

base_currency = input('Digite a moeda base: ').upper()
currency = input("Digite a moeda desejada: ").upper()

#buscando valores
response = httpx.get(url=f'https://api.exchangerate.host/latest?base={base_currency}').json()
currency_data = response['rates']

print(f'1{base_currency} vale {currency_data.get(currency)}{currency}')