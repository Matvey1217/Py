

def even_number(n):


    print(f"Парні числа від 1 до {n} :")


    for i in range(n,  0, -1):
        if i % 2 == 0:
            print(i)

n = int(input("Напишіть число n: "))

even_number(n)

