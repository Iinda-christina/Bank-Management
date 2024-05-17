Import sqlite3

# Function to create a new account
Def create_account(conn, name, balance):
    Cursor = conn.cursor()
    Cursor.execute(“INSERT INTO accounts (name, balance) VALUES (?, ?)”, (name, balance))
    Conn.commit()
    Print(“Account created successfully.”)

# Function to deposit money into an account
Def deposit(conn, account_id, amount):
    Cursor = conn.cursor()
    Cursor.execute(“UPDATE accounts SET balance = balance + ? WHERE id = ?”, (amount, account_id))
    Conn.commit()
    Print(“Deposited successfully.”)

# Function to withdraw money from an account
Def withdraw(conn, account_id, amount):
    Cursor = conn.cursor()
    Cursor.execute(“SELECT balance FROM accounts WHERE id = ?”, (account_id,))
    Current_balance = cursor.fetchone()[0]
    If current_balance >= amount:
        Cursor.execute(“UPDATE accounts SET balance = balance - ? WHERE id = ?”, (amount, account_id))
        Conn.commit()
        Print(“Withdrawn successfully.”)
    Else:
        Print(“Insufficient funds.”)

# Function to check balance of an account
Def check_balance(conn, account_id):
    Cursor = conn.cursor()
    Cursor.execute(“SELECT balance FROM accounts WHERE id = ?”, (account_id,))
    Balance = cursor.fetchone()[0]
    Print(f”Account balance: {balance}”)

# Main function
Def main():
    Conn = sqlite3.connect(“:memory:”)
    Cursor = conn.cursor()

    # Create table
    Cursor.execute(‘’’CREATE TABLE accounts
                     (id INTEGER PRIMARY KEY, name TEXT, balance REAL)’’’)
    While True:
        Print(“\n1. Create Account”)
        Print(“2. Deposit”)
        Print(“3. Withdraw”)
        Print(“4. Check Balance”)
        Print(“5. Exit”)
        Choice = input(“Enter your choice: “)
        If choice == ‘1’:
            Name = input(“Enter name: “)
            Balance = float(input(“Enter initial balance: “))
            Create_account(conn, name, balance)
        Elif choice == ‘2’:
            Account_id = int(input(“Enter account id: “))
            Amount = float(input(“Enter amount to deposit: “))
            Deposit(conn, account_id, amount)
        Elif choice == ‘3’:
            Account_id = int(input(“Enter account id: “))
            Amount = float(input(“Enter amount to withdraw: “))
            Withdraw(conn, account_id, amount)
        Elif choice == ‘4’:
            Account_id = int(input(“Enter account id: “))
            Check_balance(conn, account_id)
        Elif choice == ‘5’:
            Print(“Thank you for using the Bank Management System!”)
            Break
        Else:
            Print(“Invalid choice. Please enter a valid option.”)
    Conn.close()
If __name__ == “__main__”:
    Main()
