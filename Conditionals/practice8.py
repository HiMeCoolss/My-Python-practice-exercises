def pig_latin(word):
    first = word[0]
    if first in ("i", "o", "u", "a", "e"):
        word += "way"
        return word
    else:
        rest = word[1:]
        rest += first + "ay"
        return rest

print(pig_latin("pig"))
print(pig_latin("hello"))
print(pig_latin("owl"))

#OR:

def pig_latin(word):
    return (word[0] == "i" 
            or word[0] == "o" 
            or word[0] == "u" 
            or word[0] == "a" 
            or word[0] == "e")

def test(word):
    first = word[0]
    if pig_latin(word):
        word += "way"
        return word
    else:
        rest_of_word = word[1:]
        rest_of_word += first + "ay"
        return rest_of_word

print(test("pig"))
print(test("hello"))
print(test("owl"))



