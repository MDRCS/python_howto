
if __name__ == "__main__":

    # Lists have take larger size in memory than tuples 

    li = [1, 2, 3]
    tu = (1, 2, 3)

    print(li.__sizeof__(), tu.__sizeof__())

    # Example showing different use cases of using Lists versus Tuples

    # Immutable and Heterogenous
    task_one = ("16/07/2025 03:17:243445", "user_one", "Groceries")
    task_two = ("25/08/2025 22:45:243445", "user_one", "Laundery")
    task_three = ("30/09/2025 14:36:243445", "user_one", "Walking my dog")

    # Mutable and Homogenous
    tasks = [task_one, task_two, task_three]

    print(tasks)