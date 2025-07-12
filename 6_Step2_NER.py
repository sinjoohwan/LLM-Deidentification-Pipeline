import spacy
import json

# 모델 로드
nlp = spacy.load("ko_core_news_lg")

def mask_entities(text):
    doc = nlp(text)
    for ent in doc.ents:
        if ent.label_ in ["PER", "LOC", "ORG", "DATE"]:  # 필요시 더 추가
            text = text.replace(ent.text, f"[{ent.label_}]")
    return text
