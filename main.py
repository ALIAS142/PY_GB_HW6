# 1. Арифметической прогрессией называют числовую последовательность,
# каждый последующий член которой равен предшествующему, сложенному с одним и тем же числом.
# Пример 1: 3, 5, 7, 9, 11, ... (Первый член последовательности равен 3,
# затем к каждому прибавляется одно и то же число 2.)

# Задать размер массива:
a = []
for _ in range(int(input())):
    a.append(int(input()))

# or list comprehention:
# Using list comprehension to iterate through loop
List = [character for character in [1, 2, 3]]

# Displaying list
print(List)



# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
