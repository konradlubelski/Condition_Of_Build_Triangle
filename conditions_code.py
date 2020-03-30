def is_positive_number(x):
    if (x>0 and (isinstance(x, int) or isinstance(x, float))):
        return True
    else:
        return False

def code_of_condition(a, b, c):

    if (is_positive_number(a) and is_positive_number(b) and
    is_positive_number(c)):

        list_with_sides = [a, b, c]
        
        sorted_list = sorted(list_with_sides)

        if (sorted_list[0]+sorted_list[1]>sorted_list[2]):
            print("if we have this sides it's possible built triangle")
            return True
        
        else:
            print("a triangle cannot be built from these lengths of the sides of a triangle")
        
    else:
        print("please enter a type: (float or integer) and positive lengths of sides")

code_of_condition(-3,5,6)