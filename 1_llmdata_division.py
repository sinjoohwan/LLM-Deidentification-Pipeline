import json
import random

# 원본 JSONL 경로
input_path = r"C:\train.jsonl"  # ← 정확한 위치


# 출력 파일 경로
train_out = r"C:\train_split.jsonl"
valid_out = r"C:\valid_split.jsonl"
test_out  = r"C:\test_split.jsonl"

print("📦 원본 파일 불러오는 중...")
# 1. 원본 읽기
with open(input_path, "r", encoding="utf-8") as f:
    lines = f.readlines()

total = len(lines)
print(f"✅ 총 {total:,}개의 항목 로드 완료")

# 2. 셔플
print("🔀 데이터를 무작위로 셔플 중...")
random.shuffle(lines)

# 3. 분할 인덱스 계산
train_end = int(total * 0.8)
valid_end = train_end + int(total * 0.1)

# 4. 데이터 분할
train_set = lines[:train_end]
valid_set = lines[train_end:valid_end]
test_set  = lines[valid_end:]

print(f"📊 분할 완료: train={len(train_set):,}, valid={len(valid_set):,}, test={len(test_set):,}")

# 5. 저장 함수 정의
def save_jsonl(path, dataset, name):
    print(f"💾 {name} 저장 중 → {path} ({len(dataset):,}개 항목)")
    with open(path, "w", encoding="utf-8") as f:
        for i, item in enumerate(dataset):
            f.write(item.strip() + "\n")
            if (i+1) % 500000 == 0:
                print(f"   ...{i+1:,}개 저장 완료")

# 6. 파일 저장
save_jsonl(train_out, train_set, "train")
save_jsonl(valid_out, valid_set, "valid")
save_jsonl(test_out,  test_set,  "test")

print("✅ 전체 분할 및 저장 완료!")
