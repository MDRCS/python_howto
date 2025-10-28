from pprint import pprint
import re

if __name__ == "__main__":
    # intial input
    fruit0 = "banana"
    fruit1 = "apple"
    fruit2 = "cherry"


    # desired output
    liked_fruits = "banana, apple, cherry"
    liked_fruits = ", ".join([fruit0, fruit1, fruit2]) # this str class method accept only Iterables (Lists, Tuples, Dict).
    print(liked_fruits)

    # Automatic String Literal Construction
    
    settings = {"font_size": "large", "font": "Arial", "color": "black", "align": "center"}
    styles = f"font-size={settings['font_size']}, " \
             f"font={settings['font']}, " \
             f"color={settings['color']}, " \
             f"align={settings['align']}" # \ Backslashes are important to avoid putting all in one line

    # SPLITS

    # intial input
    visited_countries = "United states, China, France, Poland"

    # desired output
    countries = ["United states", "China", "France", "Poland"]
    countries = visited_countries.split(", ")
    print(countries)

    task_data = """1001,Homework,5
                   1002,Laundry,3
                   1003,Grocery,4"""
    processed_tasks = []
    for line in task_data.split("\n"):
        processed_task = line.strip().split(",")
        processed_tasks.append(processed_task)
    
    pprint(processed_tasks)

    # Two separators strings

    # Solution 1
    messy_data = "banana, apple_juice, grapes_smoothy"
    items_list = []

    for item in messy_data.split(","):
        if item.find("_"):
            items_list.extend(item.split("_"))
        else:
            items_list.append(item)

    print(items_list)

    # Solution 2
    items_list = []
    messy_data = messy_data.replace("_", ",")

    for item in messy_data.split(","):
        items_list.append(item.strip())
    
    print(items_list)

    # Solution 3
    
    items_list = re.findall("\w+", messy_data)
    print(items_list)






