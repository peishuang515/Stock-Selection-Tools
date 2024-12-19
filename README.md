Stock Selection Tool
The Stock Selection Tool is a Python-based application that helps users analyze historical stock prices using the Yahoo Finance API. It features user registration, login, and the ability to save and view analyzed data.

Features
User Authentication
Register: New users can create an account with an email and password.
Login: Existing users can securely access their account.
Stock Data Analysis
Retrieve historical stock prices using Yahoo Finance.
Perform analyses such as:
Latest closing price.
Average closing price.
Percentage change over a date range.
Highest and lowest closing prices.
Data Storage
Save analyzed stock data in a CSV file for future reference.
View previously saved stock records.
Prerequisites
Ensure the following software and libraries are installed on your system:

Python: Version 3.7 or higher.
Required Python libraries:
yfinance
pandas

Project Structure
The project consists of the following files:

   .
   ├── main.py              # Main script to run the program
   ├── functions.py         # Helper functions for registration, authentication, and analysis
   ├── user_credentials.csv # File to store user credentials (created automatically)
   ├── user_data.csv        # File to store user interaction data (created automatically)
   └── README.md            # Instructions for setup and usage