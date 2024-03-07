import multiprocessing
import time


# Функція для виконання тестового кейсу
def run_test(test_case):
    # Виконання тестувального коду
    print(f"Running test case {test_case}")
    time.sleep(1)  # Симуляція тривалості виконання тесту
    print(f"Test case {test_case} completed")


if __name__ == "__main__":
    # Список тестових кейсів
    test_cases = [1, 2, 3, 4, 5]

    # Запуск паралельних процесів для виконання кожного тестового кейсу
    with multiprocessing.Pool() as pool:
        pool.map(run_test, test_cases)
