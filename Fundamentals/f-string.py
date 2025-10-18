

if __name__ == "__main__":

    name = "Homework"
    urgency = 5
    print(f"Name: {name}; Urgency Level: {urgency}")

    # List
    tasks = ["Homework", "Laundry"]
    assert f"Tasks: {tasks}" == "Tasks: ['Homework', 'Laundry']"

    # Tuple
    tasks = ("Homework", "Complete Physics Assignments.")
    assert f"Tasks: {tasks}" == "Tasks: ('Homework', 'Complete Physics Assignments.')"

    # Dictionary 
    tasks = {"name" : "Laundry", "urgency": 3}
    assert f"Tasks: {tasks}" == "Tasks: {'name': 'Laundry', 'urgency': 3}"

    tasks_ids = [1, 2, 3]
    tasks_names = ["Laundry", "Homework", "Night Walk"]
    tasks_urgency = [3, 2, 1]

    for i in range(3):
        print(f"{tasks_ids[i]:^12} {tasks_names[i]:^12} {tasks_urgency[i]:^12}")