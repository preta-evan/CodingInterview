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
def isPalindrome(s):
    l, r = 0, len(s) - 1
    while l < r:
        if not s[l].isalnum():
            l += 1
        elif not s[r].isalnum():
            r -= 1
        elif s[l].lower() == s[r].lower():
            l += 1
            r -= 1 
        else:
            return False
    return True
##################################################################