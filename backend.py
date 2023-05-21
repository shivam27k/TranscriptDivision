from flask import Flask, render_template, request, jsonify

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/generate", methods=["POST"])
def generate():
    user_input = request.form["input"]

    lines = user_input.split("\n")
    should_extract = False
    extracted_content = []
    count = 0

    for line in lines:
        if "question begins" in line.lower():
            count += 1
            extracted_content.append("question no." + str(count) + ":\n")
            should_extract = True
        elif "question ends" in line.lower():
            should_extract = False
        elif should_extract:
            extracted_content.append(line)

    extracted_output = "\n".join(extracted_content)

    return jsonify({"output": extracted_output})


if __name__ == "__main__":
    app.run()
