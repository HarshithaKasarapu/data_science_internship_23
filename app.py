from flask import Flask, request
app = Flask(__name__)

@app.route("/upper_case")
def orginal_name():
    name=request.args.get('name')

    return f'<div><body><h3>The given name in uppercase is {str(name).upper()} </h3></body></div>'

@app.route("/")
def home_page():
    return "Welcome to my homepage!  Kindly type the your name with the following syntax /upper_case?name=yourname "

@app.route("/search")
def search_page():
    return "Welcome to Search Page"


if __name__ =='__main__':
    app.run(debug=True)
