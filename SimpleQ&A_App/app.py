# Python UI script (app.py)
import requests
import tkinter as tk
from tkinter import ttk

def get_answer(question, context):
    api_url = "http://127.0.0.1:5000/answer"
    data = {'question': question, 'context': context}
    response = requests.post(api_url, json=data)
    return response.json()['answer']

def ask_question():
    question = question_entry.get()
    context = context_entry.get("1.0", tk.END)
    answer = get_answer(question, context)
    answer_label.config(text=f"Answer: {answer}")

# Create UI
root = tk.Tk()
root.title("Q&A Application")

question_label = ttk.Label(root, text="Ask a Question:")
question_label.pack(pady=10)

question_entry = ttk.Entry(root, width=50)
question_entry.pack(pady=10)

context_label = ttk.Label(root, text="Context:")
context_label.pack(pady=10)

context_entry = tk.Text(root, height=5, width=50)
context_entry.pack(pady=10)

ask_button = ttk.Button(root, text="Ask", command=ask_question)
ask_button.pack(pady=10)

answer_label = ttk.Label(root, text="Answer: ")
answer_label.pack(pady=10)

root.mainloop()
