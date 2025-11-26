 Stock Portfolio Tracker

Decription

A simple command-line Python application that helps you **track stock quantities, calculate portfolio value, and save reports as TXT or CSV files**.

This tool is perfect for beginners learning Python or anyone wanting a lightweight personal tracker.



Features

* Add stocks with quantities
* View complete portfolio with stock prices & total value
* Save your portfolio summary to:

  * 📄 **TXT file**
  * 📊 **CSV file**
* Automatically timestamps saved files
* Clean, user-friendly menu interface



## 📚 Libraries Used

These come pre-installed with Python—no need to install anything.

csv – Used for exporting portfolio data into CSV format.

datetime – Used for generating timestamps in exported filenames.

How It Works (Functions Explained)

1. add_stock()

* Asks user for stock symbol
* Confirms it's available in the predefined stock list
* Requests quantity
* Adds shares to portfolio dictionary
* Prevents invalid entries



2. view_portfolio()

* Shows a formatted table of all stocks added
* Calculates total investment value
* Returns total value so it can be used by save functions



3. save_to_txt()

* Generates a `.txt` summary file
* Saves stock, quantity, price, and total value
* Filenames include timestamp
  Example: `portfolio_20251126_183020.txt`



4. save_to_csv()

* Exports full portfolio into CSV format
* Includes header row (Stock / Quantity / Price / Value)
* Also appends total portfolio value



5. menu()

* Main interactive loop
* Provides options to add/view/save/exit
* Handles invalid menu inputs


