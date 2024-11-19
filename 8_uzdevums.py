from transformers import pipeline
import spacy

text = "Valsts prezidents Egils Levits piedalījās pasākumā, ko organizēja Latvijas Universitāte."

nlp = spacy.load("xx_ent_wiki_sm")
doc = nlp(text)

# Initialize lists to store identified entities
persons = []
organizations = []

# Process the identified entities
for ent in doc.ents:
    if ent.label_ == 'PER':  # Person names
        persons.append(ent.text)
    elif ent.label_ == 'ORG':  # Organizations
        organizations.append(ent.text)

# Output the results
print("Personvārdi:", persons)
print("Organizācijas:", organizations)
