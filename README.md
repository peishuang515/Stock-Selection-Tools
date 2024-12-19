Features
1. User Authentication
-New users can register with an email and password.
-Existing users can log in to access the tool.

2.Stock Data Analysis
-Retrieve historical stock closing prices using Yahoo Finance.
-Analyze stock data, including:
  -Latest closing price.
  -Average price.
  -Percentage change over a date range.
  -Highest and lowest prices.
  
3.Data Storage and Viewing
-Save analyzed data to a CSV file for future reference.
-View previously saved records.

Prerequisites
-Python 3.7 or higher
-Required Python packages:
 -yfinance
 -pandas

Installation
1. Clone the Repository
git clone <repository_url>
cd stock-selection-tool

2. Install Dependencies
Install the required libraries using pip:
pip install yfinance pandas

Usage
1.Run the Application
Run the main.py script to start the Stock Selection Tool:
python main.py

2.Follow the On-Screen Prompts
-Register or log in as an existing user.
-Select options from the menu to retrieve and analyze stock data or view saved records.

3.Save and View Data
-The analyzed stock data will be saved in stock_data.csv.
-Use the "View Records" option to review past analyses.

File Structure
The project consists of the following files:
├── main.py              # Main program file
├── functions.py         # Contains all reusable functions
├── users.csv            # Stores user credentials (created automatically)
├── stock_data.csv       # Stores analyzed stock data (created automatically)
└── README.md            # Project documentation