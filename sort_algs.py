from random import randint


def partition(data_list, index1, index2, target):
    # Три указателя:
    now, equal, greater = index1, index1, index1
    for a_i in data_list[index1:index2 + 1]:
        if a_i[1] < target:
            data_list[now], data_list[equal] = data_list[equal], data_list[now]
            if equal != greater:
                data_list[greater], data_list[now] = data_list[now], data_list[greater]
            equal += 1
            greater += 1
        elif a_i[1] == target:
            data_list[greater], data_list[now] = data_list[now], data_list[greater]
            greater += 1
        # if a_i[1] > target: skip to next
        now += 1
    return equal


def quick_sort(data_list, l, r):
    if l < r:
        x = data_list[randint(l, r)][1]
        p = partition(data_list, l, r, x)
        quick_sort(data_list, l, p)
        quick_sort(data_list, p + 1, r)
