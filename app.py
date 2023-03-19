from flask import Flask, request, jsonify
import openai
import os

app = Flask(__name__)

openai.api_key = os.environ["OPENAI_API_KEY"]  # replace with your own OpenAI API key

@app.route("/prompt", methods=["POST"])
def generate_response():
    prompt = request.form.get("prompt")
    response = openai.Completion.create(
        engine="davinci",  # replace with the OpenAI engine you prefer to use
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )
    return jsonify(response.choices[0].text)

if __name__ == "__main__":
    app.run()
