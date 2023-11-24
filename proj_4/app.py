from flask import Flask, request
app = Flask(__name__)



@app.route("/")

def home_page():
    return "Welcome to HomePage!"

@app.route("/search")
def search_page():
    return "Welcome to Search Page"

@app.route("/add")
def org_name():
    a=request.args.get('a')
    b=request.args.get('b')
    return str(int(a)+int(b))




if __name__ =='__main__':
    app.run(debug=True)
