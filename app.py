from flask import Flask,render_template,request,jsonify
from chatbot import get_response
from voice import speak

app = Flask(__name__)

@app.route("/")
def home():

    return render_template("index.html")


@app.route("/chat",methods=["POST"])
def chat():

    user_message = request.json["message"]

    response = get_response(user_message)

    speak(response)

    return jsonify({"reply":response})


if __name__=="__main__":

    app.run(debug=True)