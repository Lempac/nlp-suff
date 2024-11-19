import spacy
from collections import Counter

nlp = spacy.load("en_core_web_sm")

text = '''Šeit ir dots teksts:  
"Mākoņainā dienā kaķis sēdēja uz palodzes. Kaķis domāja, kāpēc debesis ir pelēkas. Kaķis gribēja redzēt sauli, bet saule slēpās aiz mākoņiem."'''
doc = nlp(text)

word_count = Counter(token.text.lower() for token in doc if token.is_alpha)

sorted_word_count = word_count.most_common()

for word, count in sorted_word_count:
    print(f"The word '{word}' appears {count} times.")