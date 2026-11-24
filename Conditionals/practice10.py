import math

def smaller_root(a, b, c):
    if a == 0:
        return "not quadratic"
    discriminant = (b**2) - (4*a*c)
    if discriminant < 0:
        return None
    elif discriminant == 0:
        root = (-b) / (2*a)
        return root
    else:
        if a > 0:
            root = ((-b) - math.sqrt(discriminant)) / (2*a)
        else: 
            root = ((-b) + math.sqrt(discriminant)) / (2*a)
        return root

def test(a, b, c):
    root = smaller_root(a, b, c)
    if root == None:
        print("This quadratic has no real solution.")
    elif root == "not quadratic":
        print("This is not a quadratic equation.")
    else:
        print("The smaller root of the quadratic " + str(a)
            + "x^2 + " + str(b) + "x + " + str(c) + " is: " + str(root))

test(1, -3, -5)
    