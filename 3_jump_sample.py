import json

input_path = r"C:\train_data.jsonl"
output_path = r"C:\sample_100_jump.jsonl"

sample_indices = [i * 10000 for i in range(100)]  # 0, 10000, 20000, ..., 990000
sample_set = set(sample_indices)  # 빠른 검색을 위해 set 사용

output = []

with open(input_path, "r", encoding="utf-8") as fin:
    for i, line in enumerate(fin):
        if i > max(sample_indices):  # 효율성 위해 최대치 넘으면 종료
            break
        if i in sample_set:
            try:
                data = json.loads(line)
                output.append(data)
            except json.JSONDecodeError:
                continue

# 저장
with open(output_path, "w", encoding="utf-8") as fout:
    for item in output:
        fout.write(json.dumps(item, ensure_ascii=False) + "\n")

print("✅ 10000단위 점프 샘플 100개 추출 완료:", output_path)
