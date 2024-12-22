
n = int(input(""))

stocks = 0

company_name = "rayancode"

for i in range(n):
    text = input("")
    text = text.lower()
    if text == company_name:
        stocks += 1

print(stocks)