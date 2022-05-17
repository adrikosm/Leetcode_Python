"""
Complete the method/function so that it converts 
dash/underscore delimited words into camel casing. 
The first word within the output should be capitalized 
only if the original word was capitalized 
(known as Upper Camel Case, also often referred to as Pascal case).

Examples
"the-stealth-warrior" gets converted to "theStealthWarrior"
"The_Stealth_Warrior" gets converted to "TheStealthWarrior"

"""


def to_camel_case(text):
    s = text.replace("_"," ").replace("-"," ")
    s = s.split()
    if len(text) == 0:
        return text
    return s[0] + "".join(i.capitalize() for i in s[1:])

def main():
    print(to_camel_case("the-stealth-warrior"))  # Expected theStealthWarrior
    print(to_camel_case("python-camel-Case"))  # Expected PythonCamelCase
    print(to_camel_case("some_random-String_Test")) # Expected SomeRandomStringTest

if __name__ == "__main__":
    main()
