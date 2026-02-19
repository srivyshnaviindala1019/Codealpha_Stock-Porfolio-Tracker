stocks = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140
}
total_value = 0
for stock, price in stocks.items():
    qty = int(input(f"Enter quantity for {stock}: "))
    total_value += price * qty
print("Total Investment Value:", total_value)
with open("portfolio.txt", "w") as file:
    file.write(str(total_value))