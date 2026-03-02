# AI-Based-Automated-UML-Diagram-Generator
The AI-Based Automated UML Diagram Generator is an intelligent system that automatically converts Softw0are Requirement Specification (SRS) documents into UML diagrams using Natural Language Processing (NLP) and Machine Learning techniques.This project reduces manual effort ,accelerates the Software Development Life Cycle (SDLC).


AI-UML-Generator/
│
├── data/
├── models/
├── src/
│   ├── preprocessing.py
│   ├── uml_extractor.py
│   ├── relationship_classifier.py
│   ├── plantuml_generator.py
│
├── app.py
├── requirements.txt
└── README.md


Requirements.txt
spacy
streamlit
lxml
transformers
torch


After installing:

pip install -r requirements.txt
python -m spacy download en_core_web_sm
