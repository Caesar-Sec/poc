from flask import Flask, render_template

app=Flask(__name__)

@app.route('/')
def home():
    app.route('/')
    return render_template("home.html")

@app.route('/poc/')
def about():
    return render_template("poc.html")

if __name__=="__main__":
    app.run(debug=True)
