
def miniMaxSum(arr):
    arr.sort()
    mini = min(arr[:4])
    maxi = max(arr[1:])
    mini_sum = sum(arr) - maxi
    maxi_sum = sum(arr) - mini
    print(f"{mini_sum} {maxi_sum}")
    

def main():
    arr = [1,2,3,4,5] # Expected 10 , 14

    miniMaxSum(arr) 


if __name__ == '__main__':
    main()


