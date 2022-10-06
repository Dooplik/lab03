def bubble(n):
    for i in range(len(n)):
        for j in range(len(n) - 1):
            if n[j] > n[j + 1]:
                n[j], n[j + 1] = n[j + 1], n[j]
    return n


print("Введите n, а затем n чисел через enter")
n = [int(input()) for i in range(int(input()))]
print(bubble(n))
