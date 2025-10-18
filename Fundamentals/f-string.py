

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

    # Specifiers - Structure text display
    tasks_ids = [1, 2, 3]
    tasks_names = ["Laundry", "Homework", "Night Walk"]
    tasks_urgency = [3, 2, 1]
    center = '*^24' # center specifier
    for i in range(3):
        print(f"{tasks_ids[i]:{center}} {tasks_names[i]:{center}} {tasks_urgency[i]:{center}}")
    
    # Right-Left with Star * as a Padding
    """
        specifier = '^12'   # center spaces specifier
        specifier = '*^12'  # center stars specifier
        specifier = '>3'    # left spaces specifier
        specifier = '<3'    # right spaces specifier
        specifier = '*<3'   # right stars specifier
    """
    left = '*>3'
    right = '*<3'
    for i in range(3):
        print(f"{tasks_ids[i]:{left}} {tasks_names[i]:{center}} {tasks_urgency[i]:{right}}")

    