#метод фибоначи переписать через список а не рекурсивно n1, n2, n3=n1+n2 заполнять лупом

def fibonacci(n: int) -> int:
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        fb = [0,1]
        for i in range(2, n + 1):
            next_number = fb[-1] + fb[-2]
            fb.append(next_number)
        return fb[n]

print(fibonacci(10))