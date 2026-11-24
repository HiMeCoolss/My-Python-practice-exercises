def name_and_age(name, age):
    return (age >=0)

def test(name,age):
    if name_and_age(name, age):
        print(name + " is " + str(age) + " years old.")
    else:
        print("Error: Invalid age.")

    
    
test("Duy", 17)
test("Duy", -10)

