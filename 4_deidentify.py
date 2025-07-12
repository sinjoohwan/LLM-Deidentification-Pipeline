import json
import re

# Step 1: 비식별화 함수 정의
def deidentify(text):
    text = re.sub(r"[가-힣]{2,4}님", "[이름]", text)
    text = re.sub(r"\d{6}-\d{7}", "[주민번호]", text)
    text = re.sub(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", "[이메일]", text)
    text = re.sub(r"\d{3}-\d{3,4}-\d{4}", "[전화번호]", text)
    text = re.sub(r"\b\d{10,}\b", "[계좌번호]", text)
    text = re.sub(r"\d{2,4}[년./\- ]\d{1,2}[월./\- ]\d{1,2}[일]?", "[날짜]", text)
    return text

# Step 2: 파일 처리 경로 설정
input_path = "C:/train_data.jsonl"
output_path = "C:/train_step1_output.jsonl"

# Step 3: 파일 처리 및 저장
with open(input_path, "r", encoding="utf-8") as infile, \
     open(output_path, "w", encoding="utf-8") as outfile:
    count = 0
    for line in infile:
        item = json.loads(line)
        raw_input = item.get("input", "")
        masked_output = deidentify(raw_input)
        item["output"] = masked_output
        outfile.write(json.dumps(item, ensure_ascii=False) + "\n")
        count += 1
        if count % 100000 == 0:
            print(f"🔄 {count}개 처리 중...")

print(f"✅ 총 {count}개 항목 비식별화 완료 → {output_path}")

# Step 4: 검증 - 마스킹 토큰별 등장 횟수 카운트
from collections import Counter

deid_keywords = ["[이름]", "[주민번호]", "[전화번호]", "[이메일]", "[계좌번호]", "[날짜]"]
token_counter = Counter()
total_items = 0

with open(output_path, "r", encoding="utf-8") as f:
    for line in f:
        total_items += 1
        data = json.loads(line)
        output = data.get("output", "")
        for token in deid_keywords:
            token_counter[token] += output.count(token)

print(f"\n📊 총 {total_items:,}개 항목 중 마스킹 토큰별 등장 횟수:")
for token in deid_keywords:
    print(f"   {token}: {token_counter[token]:,}회")
