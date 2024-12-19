Stock Selection Tool
The Stock Selection Tool is a Python-based application that allows users to retrieve and analyze historical stock prices from Yahoo Finance. It features user authentication, stock analysis, and CSV data storage.

Features
User Registration and Login: Create and log in with secure credentials.
Stock Analysis: Retrieve historical stock prices and calculate:
Latest closing price.
Average price.
Percentage change over a date range.
Highest and lowest closing prices.
Data Storage: Save and view analysis results in CSV files.
Prerequisites
Before running the program, ensure the following:

Python: Install Python 3.7 or higher.
Visual Studio Code: Install the latest version of VS Code.
Required Python libraries:
yfinance
pandas
Install these libraries using pip:

pip install yfinance pandas
Installation Instructions
Step 1: Clone or Download the Repository
Open Visual Studio Code.
Open the Terminal in VS Code (View > Terminal or Ctrl + `` ).
Clone the repository using Git:
git clone <repository_url>
cd stock-selection-tool
Alternatively, download and extract the project as a ZIP file.
Step 2: Open the Project in VS Code
In Visual Studio Code, click on File > Open Folder.
Select the folder where the project files are stored.
File Structure
Ensure your project contains the following files:

stock-selection-tool/
│
├── main.py               # Main application script
├── functions.py          # Contains helper functions
├── users.csv             # User credentials (auto-generated after running)
├── stock_data.csv        # Saved stock analysis data (auto-generated)
├── README.md             # Project documentation
