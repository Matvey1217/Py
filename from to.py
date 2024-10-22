def numbers():

    num1 = int(input("Введи перше число: "))
    num2 = int(input("Введи друге число: "))


    start = num1
    end =  num2


    print(f"Числа от {start} до {end}:")
    for i in range(start, end + 1):
        print(i)



numbers()
