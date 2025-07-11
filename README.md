# Basic To-Do List App

## Project Overview
This is a simple console-based To-Do List application built in Python. It allows users to manage their daily tasks by providing options to add new tasks, view existing tasks, and remove completed or unwanted tasks. The application runs in a continuous loop until the user decides to exit.

## Features
- **Add Task:** Allows the user to input a new task and add it to their to-do list.
- **View Tasks:** Displays all current tasks in a numbered list, making it easy to reference. It also informs the user if the list is empty.
- **Remove Task:** Enables the user to remove a task by specifying its corresponding number from the displayed list. Includes error handling for invalid input (non-numeric input or out-of-range numbers).
- **Exit Application:** Provides an option to gracefully terminate the program.
- **User-Friendly Interface:** Presents a clear menu and provides feedback for all operations.

## How to Use
### Prerequisites
- Python 3.x installed on your system.

### Running the Application
- **Save the code:** Save the provided Python code into a file named `todo_app.py` (or any other `.py` extension).
- **Open a terminal/command prompt:** Navigate to the directory where you saved `todo_app.py`.
- **Run the script:** Execute the command:

```
python todo_app.py
```
### Interacting with the App
Upon running, you will see a main menu:
Welcome to the To-Do App!

```
1. Add a task
2. View tasks
3. Remove a task
4. Exit the app
Enter your choice (1-4):
```
#### To Add a Task:
- Enter `1 `and press Enter.
- You will be prompted: `Enter the task you want to add: `
- Type your task (e.g., `Go grocery shopping`) and press Enter.
- The app will confirm the task has been added.

**Note:** Each time you choose '1', you add one task.

#### To View Tasks:
- Enter `2 `and press Enter.
- The app will display your current tasks as a numbered list (e.g., `1. Go grocery shopping`).
- If no tasks are present, it will inform you.

#### To Remove a Task:
- Enter `3 `and press Enter.
- The app will first show you your current tasks with their numbers.
- You will be prompted: `Enter the task number you want to remove:` 
- Enter the number corresponding to the task you wish to remove (e.g., `1`) and press Enter.
- The app will confirm the task has been removed.
- **Error Handling:** If you enter invalid input (e.g., text, a number outside the range of tasks), the app will provide an error message and return to the main menu.

#### To Exit the App:
- Enter `4 `and press Enter.
- The app will print a goodbye message and close.

## Code Structure
The application's logic is primarily contained within a single Python script (todo_app.py) and is structured as follows:
- `to_do_items = []`: An empty Python `list `is initialized at the beginning of the script. This list serves as the central data storage for all active tasks.
- `while True`: **loop**: The core of the application is an infinite `while `loop. This ensures the menu is continuously displayed and the user can perform multiple actions until they explicitly choose to exit.
- **Menu Display:** Inside the loop, `print() `statements are used to present the user with a clear set of options.
- **User Input:** The `input()` function captures the user's choice (1-4).
- Conditional Logic (`if/elif/else`): A series of `if`, `elif` (else if), and `else `statements are used to process the user's choice:

**a**. `if choice == "1"`: Handles adding a task. It prompts for the task string and uses `list.append()` to add it.

**b**. `elif choice == "2"`: Handles viewing tasks. It checks if the list is empty `(len())` and, if not, uses a for loop with `enumerate(..., start=1)` to display tasks with user-friendly 1-based numbering.

**c**. `elif choice == "3"`: Handles removing a task.

- It first displays the current tasks.
- It uses a `try-except` block to gracefully handle `ValueError` if the user enters non-numeric input.
- It converts the user's 1-based input to a 0-based list index.
- A critical if statement `(0 <= actual_index_to_remove < len(to_do_items))` validates the index to prevent `IndexError` for out-of-range numbers.
- If the index is valid, `list.pop()` is used to remove the task at that position.

**d**. `elif choice == "4"`: Handles exiting the app by printing a goodbye message and using the break keyword to terminate the while loop.

**e**. `else`: Catches any invalid numerical or text input and prompts the user to try again.

## Key Concepts Demonstrated
This project effectively utilizes and reinforces several fundamental Python programming concepts:

- **Variables**: Storing user choices, tasks, and the `to_do_items` list.
- **Data Structures**: Extensive use of Lists (`to_do_items`) for storing and managing collections of tasks.
- **Input/Output**: Using `input()` to get data from the user and `print()` to display information and feedback.
- **Logic & Control Flow**:

**a**. `while Loops`: For maintaining the application's running state.

**b**. `if/elif/else Statements`: For decision-making based on user choices and list conditions.

**c**. `for Loops`: For iterating over the `to_do_items` list to display tasks.
- **Functions/Methods**:

**a**. Built-in functions like `len()`, `int()`, `enumerate()`.

**b**. List methods like append() and pop().
- **String Formatting**: Using f-strings (`f"..."`) for clear and dynamic messages.
- **Error Handling**: Basic `try-except` blocks to manage potential runtime errors (like `ValueError` for invalid input) and conditional checks for `IndexError`.
