"""
Given two sorted arrays nums1 and nums2 of size m and n respectively,
 return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).

Ex.
Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.

Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.5 
Since the arrays are equal the median is consited of 2 numbers 
2 and 3 in this case. So in order to find the median
we first add the two numbers and then divide 
(2+3) / 2 = 2.5
Explanation: merged array = [1,2,3,4] and median is 2.


Since the problem requires the solution to be in O(log (n+m)) time we cannot 
simply just add the arrays together
We will have to use binary search
"""


def findMedianSortedArrays(nums1, nums2):
        A, B = nums1, nums2
        total = len(nums1) + len(nums2)
        half = total // 2
        
        if len(B) < len(A):
            A, B = B, A
        
        left, right = 0, len(A) - 1
        while True:
            i = (left + right) // 2 #   Pointer for array A
            j = half - i - 2 #  Pointer for array B
            # Check if each pointer is out of bound
            # If yes then apply infinity to them
            Aleft = A[i] if i >= 0 else float("-infinity")
            Aright = A[i + 1] if (i + 1) < len(A) else float("infinity")


            Bleft = B[j] if j >= 0 else float("-infinity")
            Bright = B[j + 1] if (j + 1) < len(B) else float("infinity")
        
            #   Check if partitons are correct
            if Aleft <= Bright and Bleft <= Aright:
                # odd
                if total % 2:
                    return min(Aright, Bright)
                # even
                return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
            elif Aleft > Bright:
                right = i - 1
            else:
                left = i + 1




def main():
    print(findMedianSortedArrays([1, 2], [3]))  # EXPECTED 2
    print(findMedianSortedArrays([1, 2], [3, 4]))  # EXPECTED 2.5


if __name__ == "__main__":
    main()
