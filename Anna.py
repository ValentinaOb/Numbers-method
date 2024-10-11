import math

def f1(x2):
    return math.cos(x2) + 2


def f2(x1):
    return 0.8 - math.cos(2 * x1 - 1)

# Метод простої ітерації з новою умовою завершення


def simple_iteration(x1_0, x2_0, tol=(0.0269*0.001), max_iter=1000):
    print(0.0269*0.001," : K")
    x1_k = x1_0
    x2_k = x2_0
    for k in range(max_iter):
        # Зберігаємо попередні значення
        x1_prev = x1_k
        x2_prev = x2_k

        # Виконуємо ітерації
        x1_k = f1(x2_prev)
        x2_k = f2(x1_prev)

        # Обчислюємо максимальну дельту
        delta = max(abs(x1_k - x1_prev), abs(x2_k - x2_prev))

        # Виводимо результат кожної ітерації та дельту
        print(
            f"Ітерація {k + 1}: x1 = {x1_k:.6f}, x2 = {x2_k:.6f}, Δ = {delta:.6f}")

        # Перевірка умови завершення
        if delta <= tol:
            print(f'Знайдено розв’язок за {k + 1} ітерацій:')
            return x1_k, x2_k

    print(f'Максимальна кількість ітерацій ({max_iter}) досягнута')
    return x1_k, x2_k


# Початкові наближення
x1_0 = 1.8
x2_0 = 1.6

# Викликаємо метод
x1_sol, x2_sol = simple_iteration(x1_0, x2_0)

print(f'Приблизний розв’язок: x1 = {x1_sol:.6f}, x2 = {x2_sol:.6f}')