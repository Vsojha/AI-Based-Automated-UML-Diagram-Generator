import random

def assign_confidence(components):
    confidence_scores = {}

    for comp in components:
        confidence_scores[comp] = round(random.uniform(0.75, 0.98), 2)

    return confidence_scores