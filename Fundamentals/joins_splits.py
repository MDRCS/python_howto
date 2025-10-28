from pprint import pprint

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
