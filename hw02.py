# Task 1.1: Ella Zhao
#  Complete the function "read_two_ints" below:
def read_two_ints():
    # ADD a Docstring for this function
    # the return shown below is a placeholder to make sure this runs
    # TODO: complete the function instead of the line shown below
    """Read two inputs from the user and return them."""
    x = int(input("give me x: "))
    y = int(input("give me y: "))
    return x, y # the outputs of read_two_ints()

# Task 2.1:
#  Complete the function "compute_multadd" below:
def compute_multadd(a, b):
    # ADD a Docstring for this function
    # the pass shown below is a placeholder to make sure this runs
    # TODO: complete the function instead of the line shown below
    """Print the mult and add results of two variables a and b, then return the result of (a*b)/(a+b)."""
    numerator = a*b
    print("mult result:", numerator)
    denominator = a+b
    print("add result:", denominator)
    return numerator/denominator # the output of compute_multadd()

# Task 3.1:
#  Complete the function "print_fancy" below:
def print_fancy(a, b, ab_multadd):
    # ADD a Docstring for this function
    # the pass shown below is a placeholder to make sure this runs
    # TODO: complete the function instead of the line shown below
    """Print the inputs and multadd result in a fancy format."""
    print("****************")
    print("RESULTS:")
    print("first number:", a)
    print("second number:", b)
    print("multadd result:", ab_multadd)
    print("================") #set the format for printout

def main ():
    """Call the functions in sequence."""
    # ADD a Docstring for this function
    # Task 1.2:
    #  Add one line below to call read_two_ints (note that it returns two values)
    #  the call should provide no arguments
    #  store the returned values into two variables: x and y
    
    x, y =read_two_ints() #call and store the returned values of read_two_ints()

    # TODO: add your call instead of this line

    # Task 2.2:
    #  Add one line below to call multadd (note that it returns one value)
    #  the call should provide the arguments x, and y you obtained above;
    #  store the returned value in a variable called xy_multadd
    
    xy_multadd = compute_multadd(x, y) #call compute_multadd(a, b) and store the returned values for x and y

    # TODO: add your call instead of this line

    # Task 3.2:
    #  Complete The line below to call print_fancy
    #  the call should provide the arguments x, y, and xy_multadd you obtained above;

    # TODO: add your call instead of this line
    print_fancy(x, y, xy_multadd) #call the printout function


    # Do not modify this final print statement
    print("The End")

# Do not modify these two lines
if __name__ == "__main__":
    main()
