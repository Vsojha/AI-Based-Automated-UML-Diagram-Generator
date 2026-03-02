import spacy

nlp = spacy.load("en_core_web_sm")

def preprocess_text(text):
    doc = nlp(text)
    cleaned_sentences = []

    for sent in doc.sents:
        cleaned_sentences.append(sent.text.strip())

    return doc, cleaned_sentences