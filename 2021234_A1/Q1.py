def write_text_for_units_digit(n):
    if n == 0:
        return "zero"
    elif n == 1:
        return "one"
    elif n == 2:
        return "two"
    elif n == 3:
        return "three"
    elif n == 4:
        return "four"
    elif n == 5:
        return "five"
    elif n == 6:
        return "six"
    elif n == 7:
        return "seven"
    elif n == 8:
        return "eight"
    elif n == 9:
        return "nine"

def write_text_for_tens_digit(n):
    if n == 0:
        return ""
    elif n == 1:
        return "ten"
    elif n == 2:
        return "twenty"
    elif n == 3:
        return "thirty"
    elif n == 4:
        return "forty"
    elif n == 5:
        return "fifty"
    elif n == 6:
        return "sixty"
    elif n == 7:
        return "seventy"
    elif n == 8:
        return "eighty"
    elif n == 9:
        return "ninety"

def write_text_for_two_digit_number(n):
    if n < 10:
        return write_text_for_units_digit(n)
    elif n < 20:
        if n == 10:
            return "ten"
        elif n == 11:
            return "eleven"
        elif n == 12:
            return "twelve"
        elif n == 13:
            return "thirteen"
        elif n == 14:
            return "fourteen"
        elif n == 15:
            return "fifteen"
        elif n == 16:
            return "sixteen"
        elif n == 17:
            return "seventeen"
        elif n == 18:
            return "eighteen"
        elif n == 19:
            return "nineteen"
    else:
        tens_digit = n // 10
        units_digit = n % 10
        tens_text = write_text_for_tens_digit(tens_digit)
        units_text = write_text_for_units_digit(units_digit)
        if units_text == "":
            return tens_text
        else:
            return f"{tens_text} {units_text}"

number = int(input("Enter a number between 0 and 99: "))
print(write_text_for_two_digit_number(number))




