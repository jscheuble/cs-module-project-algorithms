'''
Input: an integer
Returns: an integer
'''


def eating_cookies(n):
    # Your code here

    # base cases
    if n == 0:
        return 1
    elif n < 0:
        return 0
    # recursive case
    # return sum of possibilities for 1, 2, and 3 at a time
    else:
        return eating_cookies(n - 1) + eating_cookies(n - 2) + eating_cookies(n - 3)


if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 5

    print(
        f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")
