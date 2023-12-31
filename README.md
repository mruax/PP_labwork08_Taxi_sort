# PP_labwork08_Taxi_sort
This is taxi sort! :p

author: Chernyakov M.

# Run

`python main.py`

or your default ide run alg.

# About

This python script sorts input data and calculates minimum summ of taxi rides!

Внутри реализована быстрая сортировка с разбиением списка через три указателя (partition содержит алгоритм LSD - Less/Equal/Greater), опорным элементом выбирается случайный среди всех. Для случайных данных в рамках этой задачи такой сортировки будет достаточно (сложность в среднем - O(n*logn)).
Списки также содержат индексы сотрудников, поэтому алгоритм сортировки является устойчивым.

# Examples

![Example image 1](https://github.com/mruax/PP_labwork08_Taxi_sort/blob/master/src/example1.png?raw=true)
![Example image 2](https://github.com/mruax/PP_labwork08_Taxi_sort/blob/master/src/example2.png?raw=true)

Exception coverage:
![Example image 3](https://github.com/mruax/PP_labwork08_Taxi_sort/blob/master/src/example3.png?raw=true)

Обновленный пример со словами:
![Example image 4](https://github.com/mruax/PP_labwork08_Taxi_sort/blob/master/src/example4.png?raw=true)

Обновленный пример с индексами такси:
![Example image 5](https://github.com/mruax/PP_labwork08_Taxi_sort/blob/master/src/example5.png?raw=true)
