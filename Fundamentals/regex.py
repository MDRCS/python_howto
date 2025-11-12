import re

if __name__ == "__main__":
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
    
    items_list = re.findall("\w+", messy_data) # Functional way to do the same thing
    print(items_list)

    # Or

    regex = re.compile(r"[,_]") # Object oriented Style, you don t have to understand underlaying of regex
    items_list = regex.split(messy_data)
    print(items_list)

    # Challenge

    # rsplit and split difference
    string_example = "banana, grapes, apple, kiwi"
    
    # Behave the same
    print(string_example.split(",", maxsplit=3), string_example.rsplit(",", maxsplit=3))

    # Behave Differently
    print(string_example.split(",", maxsplit=2), string_example.rsplit(",", maxsplit=2))

    # Regex Patterns

    test_string = "h hi hii hiii hiiii"
    regex_patterns = [r"hi", r"hi*", r"hi?", r"hi+",r"hi{3}", r"hi{2,3}", r"hi{2,}", r"hi??", r"hi*?", r"hi+?", r"hi{2,}?"]
    for pattern in regex_patterns:
        print(f"{pattern: <9} --> {re.findall(pattern, test_string)}")
    
    """
    hi{2,}    --> ['hii', 'hiii', 'hiiii'] # notice that for this case minimum is 2 but when we got 'hiii' he took it cause the max is infinit. (he acted greedy)
    hi??      --> ['h', 'h', 'h', 'h', 'h'] # logic is reversed here, ? means zero or one i, he took zero even if for the next cases there were 'ii's  (Lazy Quantifiers)
    hi*?      --> ['h', 'h', 'h', 'h', 'h'] # same as second example, * means zero or more i, he took zero even if for the next cases there were 'ii's  (Lazy Quantifiers)
    """

    test_string = "$#12med &\t\n"
    patterns  = [r'[12med]', r'\d', r'\D', r'\s', r'\S', r'\w', r'\W', r'.']

    for pattern in patterns:
        print(f"{pattern: <9} --> {re.findall(pattern, test_string)}")

    # Logical Operators

    result = re.findall(r'a|b', "a c d d b ab") 
    print(result) # ['a', 'b', 'a', 'b']

    result = re.findall(r'(abc)', "abc abcd abdfc") 
    print(result) # ['abc', 'abc']

    result = re.findall(r'[^a]', "aaaaaaalb") 
    print(result) # ['l', 'b']

    # Match Versus Search

    search  = re.search(r"(\w\d)+", "4g384jdsh2u")
    match  = re.match(r"(\w\d)+", "4g384jdsh2u") # checks only in the beginning of the string if doesn t find something return None
    # match = re.findall(r"(\w\d)+", "4g323jdsh2u")
    print(search, match.groups if match else 'We got None')

    # working with groups
    results = re.match(r"(\w+), (\w+)", "Homework, urgent; today") # as described in the pattern we have two groups (and third is the combination between the 3) to search for matches 
    print(results.groups(), results.group(0), results.group(1), results.group(2))
    print(results.span(0), results.span(1), results.span(2)) # same goes here

    # Others

    result = re.sub(r"\D", "-", "123,456&78*9") # Substitute : replace what matches the pattern with "-"
    print(result)
    
    # Challenge 

    text =  "abc_,abc__,abc,,__abc_,_abc"
    results = re.findall(r"(abc)+", text)
    print(results)

    text_data = """101, Homework; Complete physics and math some random nonsense
        102, Laundry; Wash all the clothes today
        54, random; record
        103, Museum; All about Egypt
        1234, random; record
        Another random record"""

    regex = re.compile(r"(\d{3}), (\w+); (.+)") # (.+) anything beside a newline
    tasks = []
    tasks_second = []
    for elem in text_data.split("\n"):
        tasks.extend(regex.findall(elem))

    assert tasks == regex.findall(text_data)
    print(tasks)

    # Label Our Extracted Groups rather than accessing by number (reducing error risk)
    # NB: Better to use Labels as show below rather than using indexes (e.g match.group(1))

    regex = re.compile(r"(?P<task_id>\d{3}), (?P<task_name>\w+); (?P<task_desc>.+)")
    tasks = []

    for elem in text_data.split("\n"):
        match = regex.match(elem)
        if match:
            print(match.groupdict()) # we can print the extracted group as a dict with labels we added above 
            tasks.append((match.group("task_id"), match.group("task_name"), match.group("task_desc")))
    
    print(tasks)