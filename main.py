from result_manager import add_result, view_results

while True:
    print("\nSTUDENT RESULT MANAGEMENT SYSTEM")
    print("1. Add Result")
    print("2. View Results")
    print("3. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        add_result()
    elif choice == "2":
        view_results()
    elif choice == "3":
        print("Goodbye!")
        break
    else:
        print("Invalid choice")
