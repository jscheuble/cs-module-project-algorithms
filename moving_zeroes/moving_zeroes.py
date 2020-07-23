'''
Input: a List of integers
Returns: a List of integers
'''


def moving_zeroes(arr):
    # Your code here

    # declare empty list and number of zeroes
    nums = []
    zero_count = 0

    for num in arr:
        # if the number is not a 0, add it to the list
        if num != 0:
            nums.append(num)
        # if the number is a 0, increment zero count
        else:
            zero_count += 1

    # add zeroes back in to the end of the list
    nums.extend([0] * zero_count)
    return nums


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")
