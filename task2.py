import matplotlib.pyplot as plt
import numpy as np
import scipy.integrate as spi

# Визначення функції та межі інтегрування
def f(x):
    return x**4+2*x**2

a = -1  # Нижня межа
b = 1  # Верхня межа
y_min = 0
y_max = 4

# Створення діапазону значень для x
x = np.linspace(-1, stop=1, num=400)
y = f(x)

# Створення графіка
fig, ax = plt.subplots()

# Малювання функції
ax.plot(x, y, 'r', linewidth=2)

# Заповнення області під кривою
ix = np.linspace(a, b, num=100)
iy = f(ix)
ax.fill_between(ix, iy, color='yellow', alpha=0.3)

# Налаштування графіка
ax.set_xlim([x[0], x[-1]])
ax.set_ylim([0, max(y) + 0.1])
ax.set_xlabel('x')
ax.set_ylabel('f(x)')

# Додавання меж інтегрування та назви графіка
ax.axhline(y=y_min, color='k', linestyle='--')
ax.axhline(y=y_max, color='k', linestyle='--')
ax.axvline(x=a, color='k', linestyle='--')
ax.axvline(x=b, color='k', linestyle='--')
ax.set_title('Графік інтегрування f(x) = x^4 + 2x^2 від ' + str(a) + ' до ' + str(b))
plt.grid()
plt.show()

# Метод Монте-Карло
def monte_carlo_integrate(func, a, b, y_min, y_max, num_points):
    x = np.random.uniform(a, b, num_points)
    y = np.random.uniform(y_min, y_max, num_points)
    under_curve = np.sum(y < func(x))
    area = (b - a) * (y_max - y_min)*(under_curve / num_points)

    return area


# Обчислення інтеграла
if __name__ == '__main__':
    result, error = spi.quad(f, a, b)
    mc_result = monte_carlo_integrate(f, a, b, y_min, y_max, num_points=1_000_000)
    print("Інтеграл (scipy):", result)
    print("Інтеграл (Монте-Карло):", mc_result)