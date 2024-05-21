# Sliding Window
##################################################################
def maxSum(arr, k):
    n = len(arr)
    if n <= k:
        print("Invalid")
        return -1
    window_sum = sum(arr[:k])
    max_sum = window_sum
    for i in range(n - k):
        window_sum = window_sum - arr[i] + arr[i + k]
        max_sum = max(window_sum, max_sum)
    return max_sum
##################################################################

# Two Pointers
##################################################################
def isPairSum(A, N, X):
    i = 0
    j = N - 1
    while i < j:
        if A[i] + A[j] == X:
            return True
        elif A[i] + A[j] < X:
            i += 1
        else:
            j -= 1
    return False
##################################################################