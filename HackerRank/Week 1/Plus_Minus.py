""" 
Given an array of integers, calculate the ratios of its elements that are positive, negative, and zero. 
Print the decimal value of each fraction on a new line with places after the decimal.
 Ex.
 arr [1,1,0,-1,-1]
 Output:
    Proportion of positive values
    Proportion of negative values
    Proportion of zeroes
    0.400000 (6 decimal points)
    0.200000
    0.200000
""" 
def plusMinus(arr):
    pr_negative = 0
    pr_positive = 0
    pr_zeroes = 0
    for i in arr:
        if i == 0:
            pr_zeroes += 1
        elif i > 0:
            pr_positive +=1
        else:
            pr_negative +=1
    print(f"{(pr_positive / len(arr)):.6f}")
    print(f"{(pr_negative / len(arr)):.6f}")
    print(f"{(pr_zeroes / len(arr)):.6f}")

def main():
    plusMinus([1,1,0,-1,-1])


if __name__ == "__main__":
    main()