"""Игра угадай число
Компьютер сам загадывает и сам угадывает число
"""

import numpy as np


def methodical_predict(number: int = 1) -> int:
    """Рандомно угадываем число.  
        Изменяем его в зависимости от того, больше оно или меньше нужного. 
        Функция принимает загаданное число и возвращает число попыток.

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0
    predict_number = np.random.randint(1, 101) 

    while predict_number != number:
        count += 1
        if predict_number > number:
            predict_number //= 2
        
        elif predict_number < number and count < 2:
            predict_number += 20
            
        elif predict_number < number and count < 3:
            predict_number += 10
            
        elif predict_number < number and count > 3:
            predict_number += 1
            
    return count


def score_game(methodical_predict) -> int:
    """За какое количство попыток в среднем за 1000 подходов угадывает наш алгоритм

    Args:
        methodical_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    #np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(10000))  # загадали список чисел

    for number in random_array:
        count_ls.append(methodical_predict(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за: {score} попыток")
    return score


if __name__ == "__main__":
    # RUN
    score_game(methodical_predict)
