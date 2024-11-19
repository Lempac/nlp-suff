import spacy
from collections import Counter

nlp = spacy.load("en_core_web_sm")

text = """Latvija ir valsts Baltijas reģionā. Tās galvaspilsēta ir Rīga, kas ir slavena ar savu vēsturisko centru un skaistajām ēkām. 
Latvija robežojas ar Lietuvu, Igauniju un Krieviju, kā arī tai ir piekļuve Baltijas jūrai. 
Tā ir viena no Eiropas Savienības dalībvalstīm."""

doc = nlp(text)

sentence_scores = Counter()

for sent in doc.sents:
    for word in sent:
        if word.is_stop == False and word.is_punct == False:
            sentence_scores[sent] += word.rank

summary_sentences = sentence_scores.most_common(2)

summary = ' '.join([str(sent[0]) for sent in summary_sentences])

print("Rezumējums:")
print(summary)
