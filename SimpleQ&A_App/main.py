# Install required packages
#pip install torch transformers flask

# Q&A Model script (qa_model.py)
from transformers import pipeline

qa_model = pipeline("question-answering")

def get_answer(question, context):
    result = qa_model(question=question, context=context)
    return result["answer"]
