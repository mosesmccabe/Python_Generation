# 0 1 1 2 3 5 8 13 21

def fibonacci_fun(num):
    prev = 0
    curr = 1
    for i in range(num):
        yield prev
        temp = prev
        prev = curr
        curr += temp

for num in fibonacci_fun(10):
    print(num)

# for i in range(10):
#     print(i)

x =int(4)
print(x)