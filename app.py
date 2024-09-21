from flask import Flask, render_template, request

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
        return render_template("prediction_result_DBS.html", r="Invalid input")

if __name__ == "__main__":
    app.run(debug=True)
