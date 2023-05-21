from flask import Flask, render_template, request, jsonify

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/generate", methods=["POST"])
def generate():
    input = request.form["input"]

    lines = input.split("\n")
    should_extract = False
    filtered_content = []
    count = 0

    for line in lines:
        if "question begins" in line.lower():
            count += 1
            filtered_content.append("\nQuestion no." + str(count) + ":\n")
            should_extract = True
        elif "question ends" in line.lower():
            should_extract = False
        elif should_extract:
            filtered_content.append(line)

    filtered_output = "\n".join(filtered_content)

    return jsonify({"output": filtered_output})


if __name__ == "__main__":
    app.run()
