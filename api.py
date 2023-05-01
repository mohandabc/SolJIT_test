from flask import Flask, jsonify
from flask_cors import CORS
from main import authenticate,get_candidatures


app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})

@app.route('/', methods=['GET'])
def get_example_data():
    access_token = authenticate()
    candidatures = get_candidatures(access_token=access_token)

    return jsonify(candidatures)

if __name__ == '__main__':
    app.run(debug=True)
