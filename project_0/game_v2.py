'''Игра угадай чеичло,
компьютер сам загадывает и сам отгадывает
'''

import numpy as np

def random_predict(number:int=1)->int:
    '''Функция с минимальным попытками угадывания чисел '''

    count = 0 # счетчик попыток
    '''В переменных low и high границы угадываемого числа'''
    low = 1
    high = 101
    predict_number = high // 2 # сужаем границы
    
    while number != predict_number: # пока эти числа не будут равны
        count += 1
        
        if number > predict_number:
            low = predict_number + 1
            
        elif number < predict_number:
            high = predict_number - 1
            
        predict_number = (low+high) // 2 # проверяем средний элимент
        
    return(count) # выход из цыкла, если угадали


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

# RUN
if __name__=='_main_':
    score_game(random_predict)
print(f'Колличество попыток: {random_predict()}')


