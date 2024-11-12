import sys
from convert import str_to_float

def process_command_line_args() -> float:
    """
    Sum valid float command-line arguments.

    Purpose:
    This function processes command-line arguments by attempting to
    convert each one to a float using the str_to_float function.
    It sums all valid float values and ignores invalid inputs.

    Input:
    - Command-line arguments passed as strings (sys.argv list).

    Output:
    - float: The sum of all valid floats.

    Data Representation:
    - Input is a list of strings (sys.argv).
    - Output is a float representing the sum of converted values.
    """
    total = 0.0
    for arg in sys.argv[1:]:
        number = str_to_float(arg)
        if number is not None:
            total += number
    return total

if __name__ == '__main__':
    print(f"Sum of command-line arguments: {process_command_line_args()}")
