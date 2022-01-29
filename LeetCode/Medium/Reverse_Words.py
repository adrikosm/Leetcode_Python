
"""
Given an input string s reverse the order of the words
 Ex.
  Input: 'the sky is blue'
  Output: 'blue is sky the'
"""

def reverse_words(s):
    rstring = ''
    for i in s[::-1].split(' '):
        rstring = rstring.strip() + " " + i[::-1].strip()
    return rstring
    

def main():
    print(reverse_words('the sky is blue')) # Expected blue is sky the


if __name__ == "__main__":
    main()
