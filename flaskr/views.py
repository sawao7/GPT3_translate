from flask import render_template, request
from flaskr import app

import openai
import os


openai.api_key = os.environ["API_KEY"]
# response = openai.Completion.create(
#     engine="davinci", prompt="Say this is a test", temperature=0, max_tokens=6)



# response = openai.Completion.create(
#     engine="text-davinci-002",
#     prompt="You: What have you been up to?\nFriend: Watching old movies.\nYou: Did you watch anything interesting?\nFriend:",
#     temperature=0.5,
#     max_tokens=60,
#     top_p=1.0,
#     frequency_penalty=0.5,
#     presence_penalty=0.0,
#     stop=["You:"]
# )


@app.route("/")
def index():
    data = get_response()
    return render_template("index.html", text=data)


@app.route("/", methods=["POST"])
def post():
    name = request.form.get('name')
    prompt = f"Translate this into 1. Japanese:\n\n{name}\n\n1."
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        temperature=0.3,
        max_tokens=100,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0
    )
    translate = response['choices'][0]['text']
    return render_template("index.html", text = translate)


def get_response():
    return "test"
