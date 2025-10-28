import re

if __name__ == "__main___":
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

    # Or

    regex = re.compile(r"[,_]") # you don t have to understand underlaying of regex
    items_list = regex.split(messy_data)

    # Challenge

    # rsplit and split difference
    string_example = "banana, grapes, apple, kiwi"
    
    # Behave the same
    print(string_example.split(",", maxsplit=3), string_example.rsplit(",", maxsplit=3))

    # Behave Differently
    print(string_example.split(",", maxsplit=2), string_example.rsplit(",", maxsplit=2))