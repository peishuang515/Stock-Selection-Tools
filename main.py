from functions import *

def main():
    print("Welcome to the Stock Selection Tool")
    users_file = "users.csv"
    stock_file = "stock_data.csv"

    # Registration or Login
    while True:
        new_user = input("Are you a new user? (yes/no): ").strip().lower()
        if new_user == "yes":
            email = input("Enter email: ")
            password = input("Enter password: ")
            status = register_user(email, password, users_file)
            if status == "User Exists":
                print("User already exists. Please log in.")
            else:
                print("Registration Successful! Logging in...")
            # Automatically log in
            while True:
                if authenticate_user(email, password, users_file):
                    print("Log In Successful!")
                    break
                else:
                    print("Login failed. Please try again.")
            break

        elif new_user == "no":
            email = input("Enter email: ")
            password = input("Enter password: ")
            if authenticate_user(email, password, users_file):
                print("Log In Successful!")
                break
            else:
                print("Invalid email or password. Try again.")
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")

    # Main Menu
    while True:
        print("\nMain Menu:")
        print("1. Stock Data Analysis")
        print("2. View Records")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            # Loop to allow multiple stock analyses
            while True:
                ticker = input("Enter stock ticker (e.g., 1155.KL): ")
                start_date = input("Enter start date (YYYY-MM-DD): ")
                end_date = input("Enter end date (YYYY-MM-DD): ")

                # Fetch closing prices
                closing_prices = get_closing_prices(ticker, start_date, end_date)

                if closing_prices is not None and not closing_prices.empty:
                    print(f"\nData Analysis for {ticker}")
                    analysis = analyze_closing_prices(closing_prices)

                    # Display results cleanly
                    print(f"Closing Price: {analysis['Closing Price']}")
                    print(f"Average: {analysis['Average']}")
                    print(f"Percentage Change: {analysis['Percentage Change']}%")
                    print(f"Highest: {analysis['Highest']}")
                    print(f"Lowest: {analysis['Lowest']}")

                    # Save data
                    save_to_csv(email, ticker, analysis, stock_file)
                    print("\nData saved successfully!")
                else:
                    print("Failed to fetch or analyze data. Please check the stock ticker or date range.")

                # Prompt to analyze again
                again = input("\nDo you want to analyze another stock? (Y/N): ").strip().lower()
                if again != 'y':
                    break

        elif choice == "2":
            print("\nSaved Stock Records:")
            read_from_csv(stock_file)

        elif choice == "3":
            print("Thank you for using the Stock Selection Tool!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
