import csv

stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 140,
    "MSFT": 330
}

total = 0

n = int(input("How many stocks do you want to enter? "))

with open("stocks.csv", "w", newline="") as file:

    writer = csv.writer(file)
    writer.writerow(["Stock", "Quantity", "Price", "Investment"])

    for i in range(n):

        stock = input("Enter stock name: ").upper()
        quantity = int(input("Enter quantity: "))

        if stock in stock_prices:

            price = stock_prices[stock]
            investment = price * quantity
            total += investment

            print(f"{stock}: {quantity} × ${price} = ${investment}")

            writer.writerow([stock, quantity, price, investment])

        else:
            print("Stock not found!")

print("\nTotal Investment = $", total)

with open("investment.txt", "w") as file:
    file.write(f"Total Investment = ${total}")

print("Results saved to stocks.csv and investment.txt")
