def interval_intersect(a,b,c,d):
    return (a<=d) and (c<=b)

def test(a,b,c,d):
    print("The intervals [" + str(a) + "," + str(b)+ "] and [" + str(c) + "," + str(b) + "]", end = " ")
    if interval_intersect(a,b,c,d):
        print("intersect.")
    else:
        print("do not intersect.")

test(1,5,4,7)
test(1,2,5,8)