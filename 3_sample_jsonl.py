import json

input_path = r"C:\train_step1_output.jsonl"
output_path = r"C:\sample_100.jsonl"

with open(input_path, "r", encoding="utf-8") as fin, open(output_path, "w", encoding="utf-8") as fout:
    for i, line in enumerate(fin):
        if i >= 100:
            break
        try:
            data = json.loads(line)
            fout.write(json.dumps(data, ensure_ascii=False) + "\n")
        except json.JSONDecodeError:
            continue  # 혹시 잘못된 줄이 있으면 건너뜀

print("✅ 샘플 100개 저장 완료:", output_path)
