import yfinance as yf
import pandas as pd
import csv
import os

# Function to register a new user
def register_user(email, password, users_file="users.csv"):
    if not os.path.exists(users_file):
        with open(users_file, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["email", "password"])  # Header row

    with open(users_file, "r") as file:
        reader = csv.reader(file)
        for row in reader:
            if row and row[0] == email:
                return "User Exists"

    with open(users_file, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([email, password])
    return "Registration Successful"

# Function to authenticate a user
def authenticate_user(email, password, users_file="users.csv"):
    if not os.path.exists(users_file):
        return False

    with open(users_file, "r") as file:
        reader = csv.reader(file)
        for row in reader:
            if row and row[0] == email and row[1] == password:
                return True
    return False

# Fetch closing prices using yfinance
def get_closing_prices(ticker, start_date, end_date):
    """
    Fetch historical closing prices for the given stock ticker and date range.
    Handles MultiIndex columns returned by Yahoo Finance.
    """
    try:
        # Suppress output during download
        stock_data = yf.download(ticker, start=start_date, end=end_date, progress=False)

        # Handle MultiIndex columns (if any)
        if isinstance(stock_data.columns, pd.MultiIndex):
            close_col = ('Close', ticker)
            if close_col in stock_data.columns:
                closing_prices = stock_data[close_col]
            else:
                raise KeyError(f"'Close' data not found for the ticker '{ticker}'")
        else:
            if 'Close' in stock_data.columns:
                closing_prices = stock_data['Close']
            else:
                raise KeyError(f"'Close' data not found for the ticker '{ticker}'")
        
        return closing_prices.rename("Close")  # Rename for consistency
    except Exception as e:
        print(f"Error: {e}")
        return None

# Analyze stock closing prices
def analyze_closing_prices(data):
    """
    Analyze closing prices: calculate average, percentage change, highest, and lowest.
    """
    average = data.mean()
    percentage_change = ((data.iloc[-1] - data.iloc[0]) / data.iloc[0]) * 100
    highest = data.max()
    lowest = data.min()

    # Return results in a clean dictionary
    results = {
        "Closing Price": f"RM {round(data.iloc[-1], 2)}",
        "Average": f"RM {round(average, 2)}",
        "Percentage Change": f"{round(percentage_change, 2)}",
        "Highest": f"RM {round(highest, 2)}",
        "Lowest": f"RM {round(lowest, 2)}",
    }
    return results


# Save data to CSV
def save_to_csv(email, ticker, analysis, filename="stock_data.csv"):
    exists = os.path.exists(filename)
    with open(filename, "a", newline="") as file:
        writer = csv.writer(file)
        if not exists:
            writer.writerow(["Email", "Stock Ticker", "Average", "Percentage Change", "Highest", "Lowest"])
        writer.writerow([email, ticker, analysis["Average"], analysis["Percentage Change"], analysis["Highest"], analysis["Lowest"]])

# Read saved data from CSV
def read_from_csv(filename="stock_data.csv"):
    if os.path.exists(filename):
        data = pd.read_csv(filename)
        print(data)
    else:
        print("No saved records found.")
