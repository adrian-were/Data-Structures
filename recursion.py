# def fibonacci(n):
#
#     if n == 1:
#         return 1
#     elif n == 2:
#         return 1
#     elif n > 2:
#         return fibonacci(n - 1) + fibonacci (n - 2)
#
# for i in range(1,5):
#     print(i, ":", fibonacci(i))


# cache = {}
#
# value = 0
#
# def fibonacci2(n):
#
#     if n in cache:
#         return cache[n]
#
#     if n == 1 or n == 2:
#         value = 1
#     elif n > 2:
#         value = fibonacci2(n - 1) + fibonacci2(n - 2)
#
#     cache[n] = value
#     return value

# for i in range(1,500):
#     print(f"{i} Term: {fibonacci2(i)}")

# from functools import lru_cache

# L - LAST, R - RECENTLY, C - CACHE
# @lru_cache(maxsize=1000)
# def fibonacci3(n):
#
#     if n == 1 or n == 2:
#         return 1
#     elif n > 2:
#         return fibonacci3(n - 1) + fibonacci3(n - 2)
#
# for i in range (1, 10000):
#     print (i, ":", fibonacci3(i))

def TowerofHanoi(n ,source, destination_rod, auxillliary_rod):

    if n == 1:
        print("Move disc 1 from source", source, "to destination", destination_rod)
        return
    TowerofHanoi(n-1, source, auxillliary_rod, destination_rod)
    print("Move disc",n," from source", source, "to destination", destination_rod)
    TowerofHanoi(n-1, auxillliary_rod, destination_rod, source)

n = 5
TowerofHanoi(n, 'A', 'B', 'C')