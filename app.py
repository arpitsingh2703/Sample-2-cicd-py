from flask import Flask, jsonify

# Make sure the variable name is 'app'
app = Flask(__name__)

@app.route("/")
def hello():
    return jsonify({
        "status": "success",
        "message": "Python app running in Docker on GCP VM via GitHub Actions!"
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
