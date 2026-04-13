# solver.py — файл с логикой расчета для удобного тестирования
def calculate_compound_interest(p, i, n):
    """
    p: начальный капитал
    i: годовая ставка
    n: количество лет
    """
    if not all(isinstance(x, (int, float)) for x in [p, i, n]):
        raise TypeError("Все аргументы должны быть числами")

    total = p * (1 + i / 100) ** n
    return f"Через {n} лет итоговая сумма составит: {total:.2f} руб."