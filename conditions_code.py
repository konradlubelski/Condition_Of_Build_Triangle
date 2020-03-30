def code_of_condition(length_1st_side_of_triangle,length_2nd_side_of_triangle,
 length_3rd_side_of_triangle):

    if ((isinstance(length_1st_side_of_triangle, float) or
        isinstance(length_1st_side_of_triangle, int) and
        length_1st_side_of_triangle > 0) and
        (isinstance(length_2nd_side_of_triangle, float) or
        isinstance(length_2nd_side_of_triangle, int) and
        length_2nd_side_of_triangle > 0) and
        (isinstance(length_3rd_side_of_triangle, float) or
        isinstance(length_3rd_side_of_triangle, int) and
        length_3rd_side_of_triangle > 0)):

        list_with_sides = [length_1st_side_of_triangle, length_2nd_side_of_triangle,
         length_3rd_side_of_triangle]
        
        sorted_list = sorted(list_with_sides)

        if (sorted_list[0]+sorted_list[1]>sorted_list[2]):
            print("if we have this sides it's possible built triangle")
            return True
        
        else:
            print("a triangle cannot be built from these lengths of the sides of a triangle")
        
    else:
        print("please enter a type: (float or integer) and positive lengths of sides")

code_of_condition(2,5,1)