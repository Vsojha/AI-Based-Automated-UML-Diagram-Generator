def classify_relationships(doc):
    relationships = []

    for token in doc:
        if token.dep_ == "nsubj" and token.head.pos_ == "VERB":
            subject = token.text.capitalize()
            objects = [child.text.capitalize()
                       for child in token.head.children
                       if child.dep_ in ["dobj", "attr"]]

            for obj in objects:
                relationships.append((subject, obj, "association"))

    return relationships