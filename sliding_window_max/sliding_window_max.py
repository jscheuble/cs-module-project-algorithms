'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''


def sliding_window_max(nums, k):
    # Your code here

    # declare result, start, and end
    res = []
    start = 0
    end = k

    while end <= len(nums):
        # declare maximum
        maximum = nums[start]
        # check if the other elements are larger than the maximum
        for i in range(start + 1, end):
            if nums[i] > maximum:
                maximum = nums[i]
        # add maximum for window to result array
        res.append(maximum)
        # increment start and end indices
        start += 1
        end += 1

    return res


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(
        f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
