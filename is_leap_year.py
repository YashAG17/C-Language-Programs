def is_leap_year(year: int) -> bool:
    """
    Checks if a given year is a leap year.

    Leap year rules:
    1. A year must be evenly divisible by 4.
    2. Years divisible by 100 are NOT leap years, 
       UNLESS they are also divisible by 400.
    """
    # Rule 1: Divisible by 4
    if year % 400 == 0:
        return True
    # Rule 2: Divisible by 100 but not 400
    if year % 100 == 0:
        return False
    # Rule 3: Divisible by 4 but not 100
    if year % 4 == 0:
        return True
        
    return False

# Concise alternative version:
# return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

# Example Usage:
# print(is_leap_year(2000)) # Output: True (Divisible by 400)
# print(is_leap_year(1900)) # Output: False (Divisible by 100 but not 400)
# print(is_leap_year(2024)) # Output: True (Divisible by 4)
