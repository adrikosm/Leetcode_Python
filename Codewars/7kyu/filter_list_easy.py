"""
Create a function that takes a lists of non negative
integer and strings and returns a new list with the strings
filtered out
Ex.
[1,2,'a',3,'b'] = [1,2,3]
"""


def filter_list(l):
  return [i for i in l if type(i) is int]




def main(): 
    print(filter_list([1,2,'a',3,'b']))
    print(filter_list([1,2,'a','b'])) # Expected [1,2]
    print(filter_list([1,'a','b',0,15])) # Expected [1,0,15]
    print(filter_list([1,2,'aasf','1','123',123]))  # Expected [1,2,123]


if __name__ == "__main__":
    main()