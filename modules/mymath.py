"""mymath - example math module"""
pi = 3.14159
def area(r):
        """area(r): return the area of a circle with radius."""
        global pi
        return(pi * r * r)

# In REPL
# >>> import mymath
# >>> mymath.__doc__
# >>> from mymath import pi
# >>> pi