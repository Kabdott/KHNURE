
from flask import Flask, request, jsonify, Response

app = Flask(__name__)

@app.route("/")
def postman():
    content_type = request.headers.get("Content-Type")

    if content_type == "application/json":
        return jsonify({"message": "json"})

    elif content_type == "application/xml":
        return Response(
            "<message>xml</message>",
            mimetype="application/xml"
        )

    else:
        return "empty", 200, {"Content-Type": "text/plain"}

if __name__ == "__main__":
    app.run(port=8000)
