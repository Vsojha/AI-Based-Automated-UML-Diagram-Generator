import streamlit as st
from src.preprocessing import preprocess_text
from src.uml_extractor import extract_components
from src.relationship_classifier import classify_relationships
from src.plantuml_generator import generate_plantuml
from src.confidence_engine import assign_confidence

st.set_page_config(page_title="AI UML Generator", layout="wide")

st.title("🚀 AI-Based Automated UML Diagram Generator")

srs_input = st.text_area("Enter SRS Document Text")

if st.button("Generate UML Diagram"):
    if srs_input.strip() == "":
        st.warning("Please enter SRS text.")
    else:
        doc, sentences = preprocess_text(srs_input)

        classes, attributes, methods = extract_components(doc)
        relationships = classify_relationships(doc)

        uml_code = generate_plantuml(classes, attributes, methods, relationships)

        confidence_scores = assign_confidence(classes)

        st.subheader("📦 Extracted Classes")
        st.write(classes)

        st.subheader("🔗 Relationships")
        st.write(relationships)

        st.subheader("📊 Confidence Scores")
        st.write(confidence_scores)

        st.subheader("📝 Generated PlantUML Code")
        st.code(uml_code, language="text")

        ##streamlit run app.py