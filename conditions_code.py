def is_positive_number(a, b, c):
    if (a>0 and b>0 and c>0):
        return True

def code_of_condition(a, b, c):

    if ((isinstance(a, float) or
        isinstance(a, int)) and
        (isinstance(b, float) or
        isinstance(b, int)) and
        (isinstance(c, float) or
        isinstance(c, int)) and
        is_positive_number(a, b, c)):

        list_with_sides = [a, b, c]
        
        sorted_list = sorted(list_with_sides)

        if (sorted_list[0]+sorted_list[1]>sorted_list[2]):
            print("if we have this sides it's possible built triangle")
            return True
        
        else:
            print("a triangle cannot be built from these lengths of the sides of a triangle")
        
    else:
        print("please enter a type: (float or integer) and positive lengths of sides")

code_of_condition(5,5,6)