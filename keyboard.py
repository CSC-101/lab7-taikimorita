from typing import List
from convert import str_to_float

def gather_numbers() -> List[float]:
    """
    Gather a list of float numbers from user input.

    Purpose:
    This function repeatedly prompts the user to enter numbers until the
    user types "done". It uses str_to_float to convert each input to a float.
    Invalid inputs are ignored. The function returns a list of valid floats.

    Input:
    - No input parameters; it reads input directly from the keyboard.

    Output:
    - List[float]: A list of valid float numbers entered by the user.

    Data Representation:
    - Inputs are strings entered by the user, converted to float where possible.
    - Outputs are a list of floats.
    """
    numbers = []
    while True:
        user_input = input("Enter a number (or 'done' to finish): ")
        if user_input.lower() == 'done':
            break
        number = str_to_float(user_input)
        if number is not None:
            numbers.append(number)
    return numbers

if __name__ == '__main__':
    numbers = gather_numbers()
    print(f"Sum of numbers: {sum(numbers)}")
