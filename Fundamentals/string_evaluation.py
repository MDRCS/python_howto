

if __name__ == "__main__":
    
    # checking if a username is alphanumeric

    bad_username = "hey@name1"
    assert bad_username.isalnum() == False

    good_username = "mdrahali23"
    assert good_username.isalnum() == True

    # checking is a username requires only letters
    
    bad_username = "heyname123"
    assert bad_username.isalpha() == False

    good_username = "mdrahali"
    assert good_username.isalpha() == True

    # Checking if a string contains only numbers

    assert "df123".isnumeric() == False
    assert "123".isnumeric() == True

    # Casting Strings to Int or Float

    def casting_number(number_str):

        try:
            casted_number = int(number_str)
        except ValueError:
            print(f"Couldn't Cast {repr(number_str)} to a number.")
        else:
            print(f"Casting {repr(number_str)} to {casted_number}")

    casting_number("23")
    casting_number("34.5")

    # Cast Strings to Lists, Dict and Tuples 

    list_numbers_str = "[1, 2, 3]"
    tuple_numbers_str = "(1, 2, 3)"
    dict_numbers_str = "{1: 'one', 2: 'two', 3: 'three'}"

    numbers_list = list_numbers_str.strip("[]").split(",")
    numbers_list_int = [int(elem) for elem in numbers_list]

    print(numbers_list_int, type(numbers_list_int[0])) # [1, 2, 3] <class 'int'>

    numbers_tuple = tuple_numbers_str.strip("()").split(",")
    numbers_tuple_int = tuple(int(elem) for elem in numbers_tuple)

    print(numbers_tuple_int, type(numbers_tuple_int[0])) # (1, 2, 3) <class 'int'>