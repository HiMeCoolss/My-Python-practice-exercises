def is_lunchtime(hour, is_am):
    return (hour == 11 and is_am) or (hour == 12 and not is_am)

def test(hour, is_am):
    print(hour, end = " ")
    if is_am:
        print("AM", end = " ")
    else: 
        print("PM", end = " ")
    if is_lunchtime(hour, is_am):
        print("is lunchtime.")
    else:
        print("is not lunch time.")

test(5, False)