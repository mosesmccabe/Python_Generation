

def generator_fun(num):
    for i in range(num):
        yield i*2


for item in generator_fun(10):
    print(item)
