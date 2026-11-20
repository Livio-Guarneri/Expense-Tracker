# ExpenseTracker

A Python application for tracking and managing personal expenses.

## Features

- Add expenses
- View all expenses
- View total expenses
- Remove a specific expense
- Remove all expenses
- Automatic data saving
- Automatic data loading
- Input validation
- JSON storage

## Technologies

- Python
- JSON
- pathlib

## Installation

Clone the repository:

```bash
git clone https://github.com/Livio-Guarneri/ExpenseTracker.git
```

Move into the project directory:

```bash
cd ExpenseTracker
```

## Run the Application

```bash
python expense_tracker.py
```

## Usage

### Add an Expense

Enter:

- Expense name
- Amount

Example:

```text
Name: Restaurant

Amount: 25
```

### View Expenses

Displays all recorded expenses.

Example:

```text
Name: Restaurant
Amount: 25

Name: Spotify
Amount: 10
```

### View Total

Displays the sum of all expenses.

Example:

```text
Total: 35
```

### Remove an Expense

Delete an expense by entering its name.

### Remove All Expenses

Clear all stored expenses.

## Data Storage

Expenses are automatically saved in a JSON file and reloaded when the application starts.

Example:

```json
[
    {
        "name": "Restaurant",
        "montant": 25
    },
    {
        "name": "Spotify",
        "montant": 10
    }
]
```

## Future Improvements

- Categories
- Expense statistics
- Charts and visualizations
- Monthly reports
- Graphical user interface (GUI)

## Author

**Livio Guarneri**