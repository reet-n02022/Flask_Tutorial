from flask import Flask

#  create route

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello World"

# multiple routes example

@app.route("/about")
def about():
    return "About Page"

@app.route("/contact")
def contact():
    return "Contact Page"

# static route

@app.route("/users")
def users():
    return "welcome to user page"  

# Dynamic route

@app.route("/user/<Name>")
def user(Name):
    return f"Hello, {Name}" 

# multiple dynamic parameters

@app.route("/students/<name>/<course>")
def students(name,course):
    return f"{name} is learning {course}" 

@app.route("/user_id/<id>")
def user_id(id):
    return f"Hello, {id}" 

# url converter

@app.route("/user_id1/<int:id>")
def user_id1(id):
    return f"user id: {id}" 

@app.route("/price/<float:amount>")
def price(amount):
    return f"price: {amount}" 

@app.route("/user_id2/<string:id>")
def user_id2(id):
    return f"user id: {id}"

@app.route("/files/<path:file_path>")
def files(file_path):
    return file_path

@app.route("/student/<uuid:id1>")
def student(id1):
    return str(id1)

if __name__ == "__main__":
    app.run(debug = True)