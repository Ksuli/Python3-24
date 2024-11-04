import json

def task() -> float:
    with open('input.json', 'r', encoding='utf-8') as f:
        data = json.load(f)

    total_sum = sum(d['score'] * d['weight'] for d in data)

    return round(total_sum, 3)

print(task())