from flask import Flask, render_template, request
import google.generativeai as genai
import os

model = genai.GenerativeModel("gemini-1.5-flash")
# api = 'AIzaSyBdbNliHpjp3Y_oM2T_f7RkmQhg7xk12o8'
api = os.getenv("MAKERSUITE")

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    return render_template("index.html")

@app.route("/prediction_DBS", methods=["GET", "POST"])
def prediction_DBS():
    return render_template("prediction_DBS.html")

@app.route("/prediction_result_DBS", methods=["GET", "POST"])
def prediction_result_DBS():
    q = request.form.get("q")  # Check if q is being retrieved properly
    if q:
        q = float(q)
        r = (-50.6 * q) + 90.2
        # Make sure r is being passed to the template
        return render_template("prediction_result_DBS.html", r=r)
    else:
        # Handle cases where q is None or invalid
        return (render_template("prediction_result_DBS.html", r="Invalid input"))

@app.route("/faq", methods=["GET", "POST"])
def faq():
    return render_template("faq.html")

@app.route("/q1", methods=["GET", "POST"])
def q1():
    r = model.generate_content("How should i diversify my investment portfolio")
    return render_template("q1_reply.html", r=r)

@app.route("/q2", methods=["GET", "POST"])
def q2():
    q = request.form.get("q")
    r = model.generate_content(q)
    return render_template("q2_reply.html", r=r)

if __name__ == "__main__":
    app.run(debug=True)
