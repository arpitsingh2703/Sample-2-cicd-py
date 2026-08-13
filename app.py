from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def hello():
    return jsonify({
        "status": "success",
        "message": "Python app running in Docker on GCP VM via GitHub Actions!!!!!!!!!!!!!!!!"
    })

@app.route("/health")
def health():
    return jsonify({"status": "healthy"}), 200

if __name__ == "__main__":
    # Must listen on 0.0.0.0 inside Docker containers
    app.run(host="0.0.0.0", port=8000)
