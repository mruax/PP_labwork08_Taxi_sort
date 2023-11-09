from sort_algs import quick_sort


if __name__ == "__main__":
    print("Программа Такси")

    flag = True
    n = 0
    while flag:
        n = input("Введите натуральное число N (1 ≤ N ≤ 1000) — количество сотрудников компании: ")
        try:  # проверка на корректность
            n = int(n)
            if 1 <= n <= 1000:
                flag = False
        except Exception:
            pass
    a = []
    for i in range(n):
        flag = True
        a_i = 0
        while flag:
            a_i = input(f"Введите натуральное число a_{i + 1} — расстояние от работы до дома сотрудника (в км): ")
            try:  # проверка на корректность
                a_i = int(a_i)
                if a_i > 0:
                    flag = False
            except Exception:
                pass
        a.append([i, a_i])
    b = []
    for i in range(n):
        flag = True
        b_i = 0
        while flag:
            b_i = input(f"Введите натуральное число b_{i + 1} — тариф в рублях за проезд одного километра в такси: ")
            try:  # проверка на корректность
                b_i = int(b_i)
                if b_i > 0:
                    flag = False
            except Exception:
                pass
        b.append([i, b_i])
    quick_sort(a, 0, len(a) - 1)
    quick_sort(b, 0, len(b) - 1)
    summ = 0
    print("В порядке сортировки стоимости:")
    for i in range(n):
        x = a[i][1]
        y = b[n - 1 - i][1]
        summ += x * y
        print(f"Сотрудник №{a[i][0] + 1} - {x} км * {y} руб/км = {x * y} руб.")
    print(f"Общая сумма - {summ} руб.")
