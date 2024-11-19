import spacy
from spacy.language import Language
from spacy_langdetect import LanguageDetector

nlp = spacy.load("en_core_web_sm")

@Language.factory("language_detector")
def create_language_detector(nlp, name):
    return LanguageDetector()

nlp.add_pipe("language_detector", last=True)

texts = [
    "Šodien ir saulaina diena.",
    "Today is a sunny day.",
    "Сегодня солнечный день."
]

for text in texts:
    doc = nlp(text)
    language = doc._.language
    print(f"Teksts: '{text}' - Valoda: {language['language']} (Confidence: {language['score']:.2f})")
