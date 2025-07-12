import os
import json

answer_root = r"C:\초거대AI\초거대AI 사전학습용 헬스케어 질의응답 데이터\3.개방데이터\1.데이터\Training\01.원천데이터\TS\2.답변"
results = []

for root, _, files in os.walk(answer_root):
    for fname in files:
        if not fname.endswith(".json"):
            continue

        fpath = os.path.join(root, fname)

        with open(fpath, "r", encoding="utf-8") as f:
            try:
                data = json.load(f)
            except json.JSONDecodeError:
                print(f"⚠️ JSON decode error: {fpath}")
                continue

            ans = data.get("answer", {})
            raw_text = " ".join([
                ans.get("intro", ""),
                ans.get("body", ""),
                ans.get("conclusion", "")
            ]).strip()

            if not raw_text:
                continue

            results.append({
                "instruction": "다음 문장에서 개인정보를 비식별화하세요.",
                "input": raw_text,
                "output": ""
            })

            if len(results) % 10000 == 0:
                print(f"🔄 현재 {len(results)}개 항목 처리 중...")

# 저장
output_path = r"C:\Users\HighTechM\Desktop\train.jsonl"
with open(output_path, "w", encoding="utf-8") as out_file:
    for item in results:
        out_file.write(json.dumps(item, ensure_ascii=False) + "\n")

print(f"✅ 총 {len(results)}개의 항목을 train.jsonl로 저장 완료")