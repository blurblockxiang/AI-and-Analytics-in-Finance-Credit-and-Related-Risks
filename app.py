from flask import Flask, render_template, request
import google.generativeai as genai
import os

# Initialize the generative model
model = genai.GenerativeModel("gemini-1.5-flash")
api = os.getenv("MAKERSUITE")
genai.configure(api_key=api)

# Create the Flask application
app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    return render_template("index.html")

@app.route("/prediction_DBS", methods=["GET", "POST"])
def prediction_DBS():
    return render_template("prediction_DBS.html")

@app.route("/prediction_result_DBS", methods=["GET", "POST"])
def prediction_result_DBS():
    q = request.form.get("q")  # Retrieve input value
    if q:
        try:
            q = float(q)
            r = (-50.6 * q) + 90.2  # Perform the calculation
            return render_template("prediction_result_DBS.html", r=r)  # Pass result to template
        except ValueError:
            return render_template("prediction_result_DBS.html", r="Invalid input")  # Handle conversion error
    else:
        return render_template("prediction_result_DBS.html", r="No input provided")  # Handle missing input

@app.route("/faq", methods=["GET", "POST"])
def faq():
    return render_template("faq.html")

@app.route("/q1", methods=["GET", "POST"])
def q1():
    r = model.generate_content("How should I diversify my investment portfolio?")  # Added proper question format
    return render_template("q1_reply.html", r=r)

@app.route("/q2", methods=["GET", "POST"])
def q2():
    q = request.form.get("q")  # Retrieve input value
    if q:
        r = model.generate_content(q)  # Pass user question to the model
        return render_template("q2_reply.html", r=r)  # Return the response
    else:
        return render_template("q2_reply.html", r="No input provided")  # Handle missing input

@app.route("/predict_creditability", methods=["GET", "POST"])
def predict_creditability():
    q = request.form.get("q")  # Retrieve input value
    if q:
        try:
            q = float(q)
            r = (-0.00012486 * q) + 1.27724011  # Corrected formula (removed the opening bracket)
            return render_template("predict_creditability_result.html", r=r)  # Pass result to template
        except ValueError:
            return render_template("predict_creditability.html", r="Invalid input")  # Handle conversion error
    else:
        return render_template("predict_creditability.html", r="No input provided")  # Handle missing input

if __name__ == "__main__":
    app.run(debug=True)
