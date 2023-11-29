from flask import Flask, render_template, request
from Chatterbot import ChatBot
from Chatterbot.trainers import ChatterBotCorpusTrainer

app = Flask(__name__)

# Create a chatbot instance
chatbot = ChatBot("MyBot")
trainer = ChatterBotCorpusTrainer(chatbot)
trainer.train("chatterbot.corpus.english")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get_response", methods=["POST"])
def get_response():
    user_message = request.form["user_message"]
    response = chatbot.get_response(user_message)
    return {"response": str(response)}

if __name__ == "__main__":
    app.run(debug=True)
