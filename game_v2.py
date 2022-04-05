'''Игра угадай чеичло,
компьютер сам загадывает и сам отгадывает
'''

import numpy as np

def random_predict(number:int=1)->int:
    '''Args:
        number(int, optional):Загаданное число.Defaults to 1.
        Returns:
            int: Число попыток
    '''

    count = 0
    while True:
        count += 1
        predict_number = np.random.randint(1, 101)# предпологаемое число
        if number == predict_number:
            break # выход из цикла, если угадали
    return(count)


def score_game(random_predict) -> int:
    '''За какое колличество попыток в среднем из 1000 подходов угадывает наш алгоритм
    Args:
        random_predikt([type]): функция угадывания
    Returns:
        int: среднее колличество попыток
    '''
    count_ls = [] # список для сохранения колличества попыток
    np.random.seed(1) # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=1000) # загадали список чисел
    
    for number in random_array:
        count_ls.append(random_predict(number))
    
    score = int(np.mean(count_ls)) # находим среднее колличество попыток
    print(f'Ваш алгоритм угадывает число в среднем за: {score} попыток')
    return(score)
score_game(random_predict)
#print(f'Колличество попыток: {random_predict()}')