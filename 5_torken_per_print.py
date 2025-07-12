import json

# 입력 및 출력 경로
input_path = "C:/train_step1_output.jsonl"
output_path = "C:/sample_masked_output.jsonl"

# 마스킹 토큰과 해당 샘플 보관용 딕셔너리
token_tags = {
    "[이름]": [],
    "[주민번호]": [],
    "[전화번호]": [],
    "[이메일]": [],
    "[계좌번호]": [],
    "[날짜]": []
}

# 입력 파일에서 각 토큰별 최대 10개 수집
with open(input_path, "r", encoding="utf-8") as f:
    for line in f:
        data = json.loads(line)
        output = data.get("output", "")

        for token in token_tags:
            if token in output and len(token_tags[token]) < 10:
                token_tags[token].append(data)

# 하나의 리스트로 합치기
all_samples = []
for token, samples in token_tags.items():
    all_samples.extend(samples)

# 중복 제거 (동일한 행이 여러 태그에 걸리는 경우)
seen = set()
unique_samples = []
for item in all_samples:
    key = json.dumps(item, ensure_ascii=False)
    if key not in seen:
        seen.add(key)
        unique_samples.append(item)

# 파일로 저장
with open(output_path, "w", encoding="utf-8") as out_f:
    for item in unique_samples:
        out_f.write(json.dumps(item, ensure_ascii=False) + "\n")

print(f"✅ 총 {len(unique_samples)}개 샘플 저장 완료 → {output_path}")
