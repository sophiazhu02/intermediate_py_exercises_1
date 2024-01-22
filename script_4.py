def get_valid_int_input(prompt):
    while True:
        try:
            user_input = int(input(prompt))
            return user_input
        except ValueError:
            print("Invalid input. Please enter an int.")


sum_result = 0
for i in range(5):
    user_input = get_valid_int_input(f"Enter int #{i + 1}: ")
    sum_result += user_input

print("Your sum is", sum_result)


