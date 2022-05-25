""" 
My friend John and I are members of the "Fat to Fit Club (FFC)". 
John is worried because each month a list with the weights of members is 
published and each month he is the last on the list which means he is the 
heaviest.I am the one who establishes the list so I told him: 
"Don't worry any more, I will modify the order of the list". 
It was decided to attribute a "weight" to numbers. The weight of a number 
will be from now on the sum of its digits. For example 99 will have 
"weight" 18, 100 will have "weight" 1 so in the list 100 will come before 99.
Given a string with the weights of FFC members in normal order can you give this 
string ordered by "weights" of these numbers?

Ex.
"56 65 74 100 99 68 86 180 90" ordered by numbers weights becomes: 

"100 180 90 56 65 74 68 86 99"

"""


def order_weight(strng):
    item = sorted(strng.split(' '))
    value = sorted(item, key=find_weight)
    return ' '.join(value)


def find_weight(weight):
    return sum([int(item) for item in weight])


def order_weight_one_liner(strg):
    return ' '.join(sorted(sorted(strg.split(' ')), key=lambda x: sum(int(c) for c in x)))


def main():
    print(order_weight("55 63 42 100"))
    print(order_weight("55 56 77 100 99 110"))
    print(order_weight("56 65 74 100 99 68 86 180 90"))
    print(order_weight("2000 10003 1234000 44444444 9999 11 11 22 123"))


if __name__ == "__main__":
    main()
