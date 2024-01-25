"""
Find the Equilibrium Index of an Array.
Reference: https://www.geeksforgeeks.org/equilibrium-index-of-an-array/

Python doctest can be run with the following command:
python -m doctest -v equilibrium_index_in_array.py

Given a sequence arr[] of size n, this function returns
an equilibrium index (if any) or -1 if no equilibrium index exists.

The equilibrium index of an array is an index such that the sum of
elements at lower indexes is equal to the sum of elements at higher indexes.



Example Input:
arr = [-7, 1, 5, 2, -4, 3, 0]
Output: 3

3 is an equilibrium index, because: 
A[0] + A[1] + A[2] = A[4] + A[5] + A[6]

"""
def equilibrium_index_arr_sum(arr):
    """
    Find the equilibrium index of an array using array sum 

    Args:
        arr (list[int]): The input array of integers.

    Returns:
        int: The equilibrium index or -1 if no equilibrium index exists.

    Examples:
        >>> equilibrium_index([-7, 1, 5, 2, -4, 3, 0])
        3
        >>> equilibrium_index([1, 2, 3, 4, 5])
        -1
        >>> equilibrium_index([1, 1, 1, 1, 1])
        2
        >>> equilibrium_index([2, 4, 6, 8, 10, 3])
        -1
    """
    total = sum(arr)
    left = 0
    for i, a in enumerate(arr):
        total -= a
        if left == total:
            return i
        left += a
    return -1

if __name__ == "__main__":
    arr = [-7, 1, 5, 2, -4, 3, 0]
    print("Equilibrium Index for {0} is {1}",arr,equilibrium_index_arr_sum(arr))
    arr = [1, 2, 3, 4, 5]
    print("Equilibrium Index for {0} is {1}",arr,equilibrium_index_arr_sum(arr))
    arr = [1, 1, 1, 1, 1]
    print("Equilibrium Index for {0} is {1}",arr,equilibrium_index_arr_sum(arr))
    arr = [2, 4, 6, 8, 10, 3]
    print("Equilibrium Index for {0} is {1}",arr,equilibrium_index_arr_sum(arr))
