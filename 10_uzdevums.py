from transformers import pipeline

translator = pipeline("translation", model="Helsinki-NLP/opus-mt-lv-en")

latvian_texts = [
    "Labdien! Kā jums klājas?",
    "Es šodien lasīju interesantu grāmatu."
]

translated_texts = translator(latvian_texts, max_length=40)

for original, translated in zip(latvian_texts, translated_texts):
    print(f"Latviešu: {original} \nAngļu: {translated['translation_text']}\n")
