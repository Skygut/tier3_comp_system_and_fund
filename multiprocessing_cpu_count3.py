"""
Для моделювання паралельних алгоритмів за допомогою бібліотеки multiprocessing 
ми можемо створити простий приклад паралельного обчислення, який може бути 
поділений на незалежні частини для обробки на окремих процесах. 
Ось невеликий приклад, де ми реалізуємо паралельний алгоритм сортування 
списку чисел:"""

import multiprocessing
import random


# Функція для сортування частини списку
def sort_chunk(chunk):
    return sorted(chunk)


if __name__ == "__main__":
    # Генерація великого списку чисел
    data_size = 10000
    data = [random.randint(0, 1000) for _ in range(data_size)]

    # Розділення даних на частини для паралельного сортування
    num_cores = multiprocessing.cpu_count()
    chunk_size = len(data) // num_cores if num_cores > 0 else 1
    data_chunks = [data[i : i + chunk_size] for i in range(0, len(data), chunk_size)]

    # Запуск паралельних процесів для сортування кожної частини даних
    with multiprocessing.Pool(processes=num_cores) as pool:
        sorted_chunks = pool.map(sort_chunk, data_chunks)

    # Об'єднання результатів сортування
    sorted_data = []
    for chunk in sorted_chunks:
        sorted_data.extend(chunk)

    # Виведення відсортованих даних
    print("Sorted Data:", sorted_data)
