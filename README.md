Stock Selection Tool
The Stock Selection Tool is a Python application that allows users to register, log in, and analyze stock data. The tool retrieves historical stock data using Yahoo Finance (yfinance library), performs analysis, and saves results for future reference.

Features
User Registration & Login: Securely register and log in using an email and password.
Stock Data Retrieval: Fetch historical stock closing prices for a given date range and stock ticker.
Data Analysis: Calculate key metrics such as:
Current Closing Price
Average Closing Price
Percentage Change
Highest and Lowest Closing Prices
Data Storage: Save analyzed stock data for future reference.
View Saved Records: Access previously saved stock data.
Main Menu Options
Register: Create a new user account.
Login: Access your account to analyze stock data.
Exit: Close the application.
After Logging In
Stock Data Analysis:
Input the stock ticker (e.g., AAPL or 1155.KL for Malaysian stocks).
Provide a start date and end date in the format YYYY-MM-DD.
View the analysis results, including the closing price, average, percentage change, highest, and lowest prices.
Save the analysis for future reference.
View Saved Data:
View previously saved stock data.
Logout:
Log out and return to the main menu.
File Structure
├── main.py             # Main program file
├── functions.py        # Contains all reusable functions
├── users.csv           # Stores user credentials (created after first registration)
├── stock_data.csv      # Stores analyzed stock data (created after first analysis)
├── requirements.txt    # Python dependencies
└── README.md           # Documentation