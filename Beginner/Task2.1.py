#Here we create a function called fromat_val to take two arguments.
def format_val(val1,val2):
    result = format(val1,val2)
    print("Result =",result)
    return result

#The 'o' is a format specifer which converts integer into octal representation
format_val(145,'o')