import json

file_path = r"C:\train_data.jsonl"  # 실제 경로

with open(file_path, "r", encoding="utf-8") as f:
    keys = set()
    for i, line in enumerate(f):
        if i > 1000: break
        try:
            data = json.loads(line)
            keys.update(data.keys())
        except:
            continue

print("파일 내 JSON 필드 구조:", keys)
