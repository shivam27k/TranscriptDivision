from flask import Flask, render_template, request, jsonify

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/generate", methods=["POST"])
def generate():
    input_text = request.form["input"]

    lines = input_text.split("\n")
    should_extract = False
    filtered_content = []
    count = 0

    for line in lines:
        if "question begins" in line:
            count += 1
            filtered_content.append("\nQuestion no." + str(count) + ":\n")
            should_extract = True
            filtered_content.append(line)
        elif "question ends" in line:
            filtered_content.append(line)
            should_extract = False
        elif should_extract:
            filtered_content.append(line)

    filtered_output = "\n".join(filtered_content)

    if not filtered_output:
        return jsonify({"output": "No extracted content found."})
    else:
        return jsonify({"output": filtered_output})


if __name__ == "__main__":
    app.run()
