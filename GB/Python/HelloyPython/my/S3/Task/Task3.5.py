def fib(n):
    if n in (1, 2):
        return 1
    else:
        return fib(n+2) - fib(n+1)
list = []
for e in range(1, 10):
    list.append(fib(e))
print(list)

# fib(n-1) + fib(n - 2)
# return fib*n - fib(n - 1)









# def fib(n):
#     if n in (1, 2):
#         return 1
#     else:
#         return fib(n-1) + fib(n - 2)
# list = []
# for e in range(1, 10):
#     list.append(fib(e))
# print(list)