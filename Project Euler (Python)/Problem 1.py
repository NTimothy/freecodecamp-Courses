"""
Problem 1
Find the sum of all the multiples of 3 or 5 below the provided parameter value number.
"""

# Returns a list of unique multiples of 3 or 5
def multiples_of_3_or_5(num):

    multiples = []
    if num > 3:
        x = 0
        while x < num:
            multiples.append(x)
            x += 3

    if num > 5:
        x = 0
        while x < num:
            multiples.append(x)
            x += 5

    unique_multiples = list(set(multiples))
    # print(unique_multiples)
    return unique_multiples


def problem1(lis):
    for i in lis:
        ans = sum(multiples_of_3_or_5(i))
        print(f"Sum of multiples of 3 or 5 below '{i}' is: {ans}")
    return

test_set = [10, 49, 1000, 8456, 19564]
problem1(test_set)

""" Output:
Sum of multiples of 3 or 5 below '10' is: 23
Sum of multiples of 3 or 5 below '49' is: 543
Sum of multiples of 3 or 5 below '1000' is: 233168
Sum of multiples of 3 or 5 below '8456' is: 16687353
Sum of multiples of 3 or 5 below '19564' is: 89301183
"""
