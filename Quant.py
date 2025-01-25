def distance(x1, y1, x2, y2):
    return ((x2 - x1)**2 + (y2 - y1)**2)**0.5


def FindUnreachableSegments(x1, y1, x2, y2, x3, y3):
    side_12 = distance(x1, y1, x2, y2)
    side_13 = distance(x1, y1, x3, y3)
    side_23 = distance(x2, y2, x3, y3)

    assert side_12 + side_13 > side_23
    assert side_13 + side_23 > side_12
    assert side_23 + side_12 > side_13

    x_list = [x1, x2, x3]
    y_list = [y1, y2, y3]

    y_dictionary = {}
    for y in y_list:
        if y in y_dictionary:
            y_dictionary[y] += 1
        else:
            y_dictionary[y] = 1

    if len(y_dictionary) == 3:
        return "The length of the uncountable segments is 0"
    elif (checkZeroSlopeSegment(y_dictionary)):
        return "The length of the uncountable segments is 0"
    else:
        lengthOfUnreachSegment = FindDistanceOfUnreachSegment(x1, y1, x2, y2, x3, y3)
        return  f"The length of the uncountable segments is {lengthOfUnreachSegment}"




def checkZeroSlopeSegment(y_dictionary):
    max_coordiante = max(y_dictionary)
    max_element_count = max(y_dictionary, key=y_dictionary.get)
    if max_coordiante == max_element_count:
        return False
    return True


def FindDistanceOfUnreachSegment(x1, y1, x2, y2, x3, y3):
    if(y2 - y1 == 0):
        return abs(x2-x1)
    elif(y3-y1 == 0):
        return abs(x3-x1)
    else:
        return abs(x3-x2)




x1 = int(input("Please enter the first x coordinate: "))
y1 = int(input("Please enter the first y coordinate: "))
x2 = int(input("Please enter the second x coordinate: "))
y2 = int(input("Please enter the second y coordinate: "))
x3 = int(input("Please enter the third x coordinate: "))
y3 = int(input("Please enter the third y coordinate: "))


print(FindUnreachableSegments(x1, y1, x2, y2, x3, y3))





