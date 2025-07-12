# LLM 개인정보 마스킹 파이프라인

본 저장소는 한국어 의료 QA 데이터셋의 직접 식별자 및 간접 식별자를 제거하기 위한 비식별화(De-identification) 파이프라인을 제공합니다.

---

## 📁 구성 파일

| 파일명 | 설명 |
|--------|------|
| `1_llmdata_division.py` | jsonl 데이터를 8:1:1 비율로 train/valid/test로 분할 |
| `2_find_scrupture.py` | json 구조 필드 자동 탐색 |
| `3_sample_jsonl.py` | 특정 조건 샘플 추출기 |
| `3_jump_sample.py` | 마스킹된 토큰별 샘플 10개씩 추출 |
| `4_deidentify.py` | 직접 식별자 정규표현식 마스킹 (이름, 이메일 등) |
| `5_token_per_print.py` | 마스킹된 토큰별 빈도 출력기 |
| `6_STEP2.py` | 간접 식별자 NER 처리 시작 코드 |
| `6_Step2_NER.py` | spaCy 기반 NER 전처리기 (KLUE NER/KoBERTNER 적용 가능) |

---

## 📦 설치 환경
로컬(Python 3.10 이상) 또는 Google Colab

```bash
pip install spacy
pip install transformers
pip install pororo
pip install fugashi
pip install sentencepiece
pip install git+https://github.com/SKTBrain/KoBERT.git
