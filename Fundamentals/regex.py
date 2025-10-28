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