from app import app

@app.route("/")
def hello():
    return "Hello api transaction"

if __name__ == "__main__":
    app.run(debug=True)