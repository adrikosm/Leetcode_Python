"""
Implement a function that accepts 3 integer values a, b, c. 
The function should return true if a triangle can be built with 
the sides of given length and false in any other case
"""


def is_triangle(a,b,c):
    if(a + b > c) and (b + c > a) and (c + a > b):
        return True
    else:
        return False


def main():
    print(is_triangle(1, 2, 2)) #Expected True
    print(is_triangle(7, 2, 2)) # Expected False
    print(is_triangle(1, 2, 3)) # Expected False
    print(is_triangle(7, 2, 2)) # Expected True
    print(is_triangle(5,3,3))  # Expected True


if __name__ == "__main__":
    main()