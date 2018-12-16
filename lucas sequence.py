# 2, 1, 3, 4, 7, 11, 18, 29
# def lucas(n):
#     if n == 0:
#         return 2
#     if n == 1:
#         return 1
#     else:
#         return lucas (n-2) + lucas (n-1)
# print(lucas(5))

def lucas(n):
    a, b = 2, 1
    for i in range(n):
        a, b = b, a + b
    return a


print(lucas(100000))
