# def power(x,n):
#     if n == 0:
#         return 1
#     else:
#         return x*power(x,n-1)
#
# print(power(5,3))

# def factorial(x):
#     if x == 1:
#         return 1
#     else:
#         return x*factorial(x-1)
#
# print(factorial(5))

# def fibonacci(n):
#     if n==1:
#         return [1]
#     elif n==2:
#         return [1,1]
#     else:
#         return fibonacci(n-1) + [fibonacci(n-1)[-1] + fibonacci(n-1)[-2]]

#print(fibonacci(10))
def toChars(s):
    s = s.lower()
    ans = ''
    for c in s:
        if c in s:
            ans = ans + c
    return ans

def is_palindrome(s):
    s = toChars(s)
    if len(s) <= 1:
        return True
    else:
        return s[0] == s[-1] and is_palindrome(s[1:-1])

#print(is_palindrome("Madam"))

print(is_palindrome("Able was I ere I saw Elba"))
