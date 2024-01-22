def count_letters(input_string):
    letter_count = {}
    for char in input_string:
        if char.isalpha():  # excludes spaces
            char_lower = char.lower()  
            letter_count[char_lower] = letter_count.get(char_lower, 0) + 1
    return letter_count

user_input = input("Enter a string: ")

result_dict = count_letters(user_input)
print(result_dict)
