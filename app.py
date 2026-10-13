from flask import Flask,request

app = Flask(__name__)

@app.route("/search")
def search():
    name = request.args.get("name","Guest") # here Guest is default
    course = request.args.get("course","Unknown") # here Unknown is default
    return f"{name} is learning {course}"


if __name__ == "__main__":
    app.run(debug = True)