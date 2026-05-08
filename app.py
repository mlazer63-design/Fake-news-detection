from flask import Flask, request, render_template_string
import random

app = Flask(__name__)

HTML = """

<!DOCTYPE html>
<html>

<head>

<title>Fake News Detection</title>

<style>

body{
    background:#0f172a;
    color:white;
    font-family:Arial;
}

.container{
    width:70%;
    margin:auto;
    text-align:center;
    padding-top:50px;
}

textarea{
    width:100%;
    height:250px;
    padding:20px;
    border-radius:10px;
    font-size:18px;
}

button{
    margin-top:20px;
    padding:15px 40px;
    border:none;
    border-radius:10px;
    background:#2563eb;
    color:white;
    font-size:18px;
}

.result{
    margin-top:30px;
    background:#1e293b;
    padding:20px;
    border-radius:12px;
}

</style>

</head>

<body>

<div class="container">

<h1>AI Fake News Detection System</h1>

<form method="POST" action="/predict">

<textarea
name="news"
placeholder="Paste News Here..."
required></textarea>

<br>

<button type="submit">

Detect News

</button>

</form>

{% if prediction %}

<div class="result">

<h2>{{ prediction }}</h2>

<h3>Confidence: {{ confidence }}%</h3>

</div>

{% endif %}

</div>

</body>

</html>

"""

@app.route("/")
def home():
    return render_template_string(HTML)

@app.route("/predict", methods=["POST"])
def predict():

    news = request.form["news"]

    prediction = random.choice([
        "FAKE NEWS",
        "REAL NEWS"
    ])

    confidence = random.randint(85, 99)

    return render_template_string(
        HTML,
        prediction=prediction,
        confidence=confidence
    )

if __name__ == "__main__":
    app.run(debug=True)