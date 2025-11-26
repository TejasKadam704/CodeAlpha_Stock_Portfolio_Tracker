import csv
from datetime import datetime

stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 310,
    "AMD": 120,
    "NVDA": 450
}

portfolio = {}  


def add_stock():
    print("\n--- Add Stock to Portfolio ---")
    stock = input("Enter stock symbol (e.g., AAPL, TSLA): ").upper()

    if stock not in stock_prices:
        print("❌ Stock not found in database!")
        print("Available stocks:", ", ".join(stock_prices.keys()))
        return

    try:
        qty = int(input("Enter quantity: "))
        if qty <= 0:
            print("❌ Quantity must be positive.")
            return
    except ValueError:
        print("❌ Invalid quantity. Enter a number.")
        return

    portfolio[stock] = portfolio.get(stock, 0) + qty
    print(f"✔ Added {qty} shares of {stock}.")


def view_portfolio():
    if not portfolio:
        print("\nYour portfolio is empty!")
        return

    print("\n--- Portfolio Summary ---")
    print("{:<10} {:<10} {:<10} {:<10}".format("Stock", "Qty", "Price", "Value"))

    total_value = 0
    for stock, qty in portfolio.items():
        price = stock_prices[stock]
        value = price * qty
        total_value += value
        print("{:<10} {:<10} {:<10} {:<10}".format(stock, qty, price, value))

    print("\nTotal Investment Value: $", total_value)
    return total_value


def save_to_txt():
    total_value = view_portfolio()
    if total_value is None:
        return

    filename = f"portfolio_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
    with open(filename, "w") as file:
        file.write("Stock Portfolio Summary\n")
        file.write("-----------------------\n")
        for stock, qty in portfolio.items():
            file.write(f"{stock}: {qty} shares @ ${stock_prices[stock]}\n")
        file.write(f"\nTotal Value: ${total_value}")

    print(f"✔ Saved portfolio to {filename}")


def save_to_csv():
    total_value = view_portfolio()
    if total_value is None:
        return

    filename = f"portfolio_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
    with open(filename, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Stock", "Quantity", "Price", "Value"])

        for stock, qty in portfolio.items():
            writer.writerow([stock, qty, stock_prices[stock], qty * stock_prices[stock]])

        writer.writerow([])
        writer.writerow(["TOTAL", "", "", total_value])

    print(f"✔ Saved portfolio to {filename}")


def menu():
    while True:
        print("\n===== STOCK PORTFOLIO TRACKER =====")
        print("1. Add Stock")
        print("2. View Portfolio")
        print("3. Save to TXT File")
        print("4. Save to CSV File")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_stock()
        elif choice == "2":
            view_portfolio()
        elif choice == "3":
            save_to_txt()
        elif choice == "4":
            save_to_csv()
        elif choice == "5":
            print("Thank you for using the Stock Tracker!")
            break
        else:
            print("❌ Invalid option. Try again.")

menu()
