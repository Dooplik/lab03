def bubble(n, route):
    for i in range(len(n)):
        for j in range(len(n) - 1):
            if route == 1:
                if n[j] > n[j + 1]:
                    n[j], n[j + 1] = n[j + 1], n[j]
            elif route == 0:
                if n[j] < n[j + 1]:
                    n[j], n[j + 1] = n[j + 1], n[j]
            else:
                print("ERROR")
    return n


print("Введите n, а затем n чисел через enter")
n = [int(input()) for i in range(int(input()))]
print("Введите направление\n1 - По возрастанию\n0 - По убыванию")
r = int(input())
print(bubble(n, r))
