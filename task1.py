import pulp

# Ініціалізація моделі
model = pulp.LpProblem("Maximize Production", pulp.LpMaximize)

# Визначення змінних
lemonade = pulp.LpVariable('Lemonade', lowBound=0, cat='Integer')  # Кількість лимонаду
fruit_juice = pulp.LpVariable('Fruit_Juice', lowBound=0, cat='Integer')  # Кількість фруктового соку

# Функція цілі (Максимізація загальної к-сті продуктів)
model += lemonade + fruit_juice, "Total Products Produced"

# Додавання обмежень
model += 2*lemonade + 1*fruit_juice <= 100, "Water Constraint"
model += 1*lemonade <= 50, "Sugar Constraint"
model += 1*lemonade <= 30, "Lemon Juice Constraint"
model += 2*fruit_juice <= 40, "Fruit Puree Constraint"

# Розв'язання моделі
model.solve()

# Вивід результатів
print("Для максимізації загальної кількості продуктів, треба:")
print(f"Виробляти продуктів 'Лимонад' - {lemonade.varValue}")
print(f"Виробляти продуктів 'Фруктовий сік' - {fruit_juice.varValue}")