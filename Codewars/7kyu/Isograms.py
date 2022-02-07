"""
An isogram is a word that has no repeating letters, consecutive or non-consecutive. 
Implement a function that determines whether a string that contains only letters is an isogram.
Assume the empty string is an isogram. Ignore letter case.
""" 

def isogram(s):
    gone = []
    for i in s:
        if i.lower() in gone:
            return False
        else:
            gone.append(i.lower())
    return True

def main():
    print(isogram("Dermatoglyphics"))
    print(isogram("aba"))
    print(isogram("moOse"))

if __name__ == "__main__":
    main()