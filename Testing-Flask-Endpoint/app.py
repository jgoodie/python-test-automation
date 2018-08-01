from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/') # http://www.localhost.com/
def home():
    return(jsonify({'message':'Hello, world!'}))

if __name__ == '__main__':
    app.run()
