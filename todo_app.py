to_do_items = []

while True: 

    print("Welcome to the To-Do App!")
    print("1. Add a task")
    print("2. View tasks")
    print("3. Remove a task")
    print("4. Exit the app")
     
    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        print("You chose to add a task")
        task = input("Enter the task you want to add: ")
        to_do_items.append(task)  
        print(f"'{task}' added successfully!")
        
    elif choice == "2":
       if len(to_do_items) == 0:
            print("No tasks available. Please add a task first.")
       else:
            print("Your current tasks are:")
            for index, item in enumerate(to_do_items, start=1):
                print(f"{index}. {item}")
            
    elif choice == "3":
        if len(to_do_items) == 0:
            print("No tasks available. Please add a task first.")
        else:
            print("Your current tasks are:")
            for index, item in enumerate(to_do_items, start=1):
                print(f"{index}. {item}")

            try:    
                index = int(input("Enter the task number you want to remove: ")) -1
                if 0 <= index < len(to_do_items):
                    final_index = to_do_items.pop(index)
                    print(f"Task '{final_index}' removed successfully!")
                else:
                    print("Invalid task number. Please try again.")
            except ValueError:
                print("Invalid input. Please enter a valid task number.")

    elif choice == "4":
        print("Exiting the app. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")

