'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''


def single_number(arr):
    # Your code here
    # sort array
    arr.sort()

    # define single number and iterator
    single = 0
    i = 0

    # loop over sorted array
    while i < len(arr):
        # if we've reached the last element in the array, it's the single number
        if i == len(arr) - 1:
            single = arr[i]
            return single
        # if the number is equal to it's right neighbor, skip the neighbor
        elif arr[i] == arr[i + 1]:
            i += 2
        # return the single number
        else:
            single = arr[i]
            return single

    return single


if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")
