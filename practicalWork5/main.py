import matplotlib.pyplot as plt
import numpy as np
import math

x = [-0.03, 0.73, -0.59, -1.59, 0.38, 1.49, 0.14, -0.62, -1.59, 1.45,
      -0.38, -1.49, -0.15, 0.63, 0.06, -1.59, 0.61, 0.62, -0.05, 1.56]

# Вариационный ряд
print("\033[32mВариационный ряд:\033[0m ")
print(sorted(x))
print()

# Экстримальные значения
print("\033[32mЭкстримальные значения:\033[0m " + str(min(x)) + ", " + str(max(x)) + ". Размах: "
      + str(max(x) - min(x)) + ".")
print()

length = len(x)

# Оценка мат. ожидания и среднеквадратическое отклонение
M = 0
for i in range(length):
    M += x[i] * x.count(x[i])
M = M / length
print("\033[32mОценка мат. ожидания:\033[0m " + str(M))
D = 0
for i in range(length):
    D += pow((x[i] - M), 2) * x.count(x[i])
D = D / length
sigma = pow(D, 0.5)
print("\033[32mСреднеквадратическое отклонение:\033[0m " + str(sigma))
print()

set_var_row = sorted(list(set(sorted(x))))
set_var_row_length = len(set_var_row)
sum = 0

# Статистический ряд
stats_row = {i: 0 for i in sorted(x)}
for i in sorted(x):
    stats_row[i] += 1
print("\033[32mСтатистический ряд:\033[0m ")
for i in stats_row:
    print(i, end=" ")
print()
for i in stats_row:
    if i < 0:
        print(stats_row[i], end="     ")
    else:
        print(stats_row[i], end="    ")
print()

print()

# Массив частостей
p = {i: 0 for i in sorted(x)}
for i in set_var_row:
    p[i] = stats_row[i] / len(sorted(x))

print("\033[32mМассив частостей для каждого из x в  x:\033[0m ")
print(p)
print()

# Интервальный статистический ряд
print("\033[32mИнтервальный статистический ряд:\033[0m ")
h = round((max(x) - min(x)) / (1 + math.log2(set_var_row_length)), 1) # Ширина интервала по формуле Стерджеса
x_first_value = min(x) - h / 2
x_last_value = x_first_value + h
count_of_x_in_interval = 0
interval_centers = []
interval_frequency = []

# Эмпирическая функция распределения
for i in set_var_row:
    if i < x_last_value:
        count_of_x_in_interval += stats_row[i]
    else:
        interval_centers.append((x_first_value + x_last_value) / 2)
        interval_frequency.append(count_of_x_in_interval / len(sorted(x)))
        print("[" + str(x_first_value) + ", " + str(x_last_value) + ") - частота:", count_of_x_in_interval, "частотность:", count_of_x_in_interval / len(sorted(x)))
        count_of_x_in_interval = 0
        x_first_value = x_last_value
        x_last_value = round(x_first_value + h, 2)
        count_of_x_in_interval += stats_row[i]
interval_centers.append((x_first_value + x_last_value) / 2)
interval_frequency.append(count_of_x_in_interval / len(sorted(x)))
print("[" + str(x_first_value) + ", " + str(x_last_value) + ") - частота:", count_of_x_in_interval, "частотность:", count_of_x_in_interval / len(sorted(x)))
print()

print("\033[32mЭмпирическая функция распределения:\033[0m ")
print(f"При x <= '{set_var_row[0]}' - 0")
previous = set_var_row[0]
sum = p[set_var_row[0]]
for i in set_var_row[1:]:
    print(f"При '{previous}' < x <= '{i}' - {sum}")
    sum = round(sum + p[i], 3)
    previous = i
print(f"При '{previous}' < x - {sum}")
print()

def F(x):
    ans = 0
    for i in set_var_row:
        if (i < x):
            ans += p[i]
    return ans

x = np.linspace(sorted(x)[0] - 1, sorted(x)[-1] + 1, 10000)
y = [F(i) for i in x]

# Создание Фигуры и Осей
figure = plt.figure()
coordinate_axes = figure.add_subplot(1, 1, 1)

# Настройка Внешнего Вида Осей
coordinate_axes.spines['left'].set_position('center')
coordinate_axes.spines['bottom'].set_position('zero')
coordinate_axes.spines['right'].set_color('none')
coordinate_axes.spines['top'].set_color('none')
coordinate_axes.xaxis.set_ticks_position('bottom')
coordinate_axes.yaxis.set_ticks_position('left')

print(interval_centers)

# Линейный график
plt.plot(x, y, 'b')
plt.show()

# Столбчатая диаграмма
plt.bar(interval_centers, interval_frequency)
plt.show()

# # Линейный график
plt.plot(interval_centers, interval_frequency)
plt.show()