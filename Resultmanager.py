def auto_add_results():
    # This automatically adds names so you don't type every time
    students = [
        ("Aisha", 80),
        ("Tolu", 75),
        ("Samuel", 90),
        ("Zainab", 88),
        ("Daniel", 70)
    ]

    with open("results.txt", "w") as file:
        for name, score in students:
            file.write(f"{name} - {score}\n")


def add_result():
    name = input("Enter student name: ")
    score = input("Enter score: ")

    with open("results.txt", "a") as file:
        file.write(f"{name} - {score}\n")

    print("Result saved successfully")


def view_results():
    try:
        with open("results.txt", "r") as file:
            print("\nSTUDENT RESULTS")
            print(file.read())
    except FileNotFoundError:
        print("No results found")
