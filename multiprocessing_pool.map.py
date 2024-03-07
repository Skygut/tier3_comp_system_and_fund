import multiprocessing


# Функція для обробки даних
def process_data(line):
    # Приклад обробки даних - у цьому випадку просто повертаємо довжину рядка
    return len(line)


if __name__ == "__main__":
    # Великий обсяг даних для обробки
    big_data = [
        "Lorem ipsum dolor sit amet",
        "consectetur adipiscing elit",
        "sed do eiusmod tempor incididunt",
        "ut labore et dolore magna aliqua",
        "Ut enim ad minim veniam",
        "quis nostrud exercitation ullamco",
    ]

    # Запуск паралельних процесів для обробки кожного елемента списку
    with multiprocessing.Pool() as pool:
        processed_results = pool.map(process_data, big_data)

    # Виведення оброблених даних
    print("Processed Data:", processed_results)
