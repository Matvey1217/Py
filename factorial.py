def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


n = int(input("Напишіть число для обчислення факторіалу: "))
print(f"Факторіал числа {n} = {factorial(n)}")

factorial(n)
