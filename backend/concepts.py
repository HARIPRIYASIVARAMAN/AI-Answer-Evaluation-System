import spacy

# Load spaCy English model
nlp = spacy.load("en_core_web_sm")

def extract_concepts(text):
    """
    Extract important noun phrases (concepts) from model answer
    """
    doc = nlp(text)
    concepts = set()

    for chunk in doc.noun_chunks:
        concepts.add(chunk.text.lower())

    return list(concepts)
