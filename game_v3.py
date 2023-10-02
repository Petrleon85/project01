"""Игра угадай число
Компьютер сам загадывает и сам угадывает число
"""
import numpy as np
def game_core_v3(number: int = 1) -> int:
    """
    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    """Решение задачи сводится к принципу каждый раз называть число,
    которое делит пополам диапазон возможных чисел"""
    # определяем нижнюю границу диапазона чисел
    minimum_value = 1
    # определяем верхнюю границу диапазона чисел
    maximum_value = 101 
    # определяем количество попыток
    count = 1
    predict_number = np.random.randint(1, 101)
    # компьютер угадывает число

    while number != predict_number:
        if (maximum_value - minimum_value) < 2:
            break 
        count += 1
       
        if predict_number > number:  # если предсказанное число больше загаданного
            maximum_value = predict_number
            predict_number = round((minimum_value + maximum_value) / 2)
        
        else:
            # если предсказанное число меньше загаданного
            minimum_value = predict_number
            predict_number = round((minimum_value + maximum_value) / 2)

    return count

def score_game(random_predict) -> int:
    """За какое количество попыток в среднем за 10000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    #np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(10000))  # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за: {score} попыток")