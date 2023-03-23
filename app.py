from flask import Flask
app = Flask(__name__)

@app.route("/testapi")
def home():
    return "Hello, this is a sample Python Web App running on Flask Framework!"

  
if __name__ == '__main__':
    app.run(debug=True)