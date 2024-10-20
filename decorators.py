def is_prime(func):
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        for i in range(2, res // 2):
            if (res % i == 0) == True:
                print("Составное")
                return res
        else:
            print("Простое")
            return res
    return wrapper

@is_prime
def sum_three(*args):
    res = 0
    for num in args:
        res += num
    return res


result = sum_three(8, 3, 6)
print(result)
