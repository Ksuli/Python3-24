import csv
import json

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"

def task() -> None:
    try:
        with open(INPUT_FILENAME, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            rows = list(reader)
            #print(f"Считанные данные: {rows}")  # Выводим считанные данные для проверки

        with open(OUTPUT_FILENAME, 'w', encoding='utf-8') as jsonfile:
            json.dump(rows, jsonfile, ensure_ascii=False, indent=4)
            #print("Данные успешно записаны в JSON файл.")  # Подтверждаем запись

    except Exception as e:
        print(f"Произошла ошибка: {e}")

if __name__ == "__main__":
    task()

    try:
        with open(OUTPUT_FILENAME, encoding='utf-8') as output_f:
            for line in output_f:
                print(line, end="")
    except FileNotFoundError:
        print("JSON файл не найден.")