from collections import defaultdict

def extract_components(doc):
    classes = set()
    attributes = defaultdict(list)
    methods = defaultdict(list)

    for token in doc:
        # Classes → Nouns
        if token.pos_ == "NOUN" and token.text.isalpha():
            classes.add(token.text.capitalize())

        # Methods → Verbs
        if token.pos_ == "VERB":
            subject = [child for child in token.children if child.dep_ == "nsubj"]
            if subject:
                cls = subject[0].text.capitalize()
                methods[cls].append(token.lemma_)

        # Attributes → Adjectives
        if token.pos_ == "ADJ":
            head = token.head.text.capitalize()
            attributes[head].append(token.text)

    return classes, attributes, methods