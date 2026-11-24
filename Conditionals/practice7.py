def print_digits(number):
    return (number > 100) or (number < 0)

def test(number):
    if not print_digits(number):
        tens = number // 10
        ones = number % 10
        print("Tens: " + str(tens) + ", ones: " + str(ones) + ".")
    else:
        print("Error: input is not a two-digit number.")

test(100)
test(27)

    