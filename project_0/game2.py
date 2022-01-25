"""Game to guess number"""

import numpy as np

# number = np.random.randint (1, 101) # Guess number

# number of attemps
count = 0

while True:
    count+=1
    predict_number = int(input("Guess number form 1 till 100\n"))
    
    if predict_number > number:
        print('Number must be smaller\n')
        
    elif predict_number < number:
        print('Number must be bigger\n')
        
    else:
        print(f'You got it! Number is {number} in {count} times')
        break # End game

def score_game(random_predict) -> int:
    """За какое количество попыток в среднем за 10000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(10000))  # загадали списоконлайн переводчик чисел

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за: {score} попытки")
    