import os
import pickle
# import pandas as pd
from flask import Flask, jsonify, request, render_template
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/predict', methods=['POST'])
def apicall():
    resp_obj = {'status': 'success'}
    post_data = request.get_json()
    # return str(request)
    r = post_data.get('r')
    g = post_data.get('g')
    b = post_data.get('b')
    if(0 <= r < 256) and (0 <= g < 256) and (0 <= b < 256):
        test = [[b,g,r]]
        with open('model_pH', 'rb') as f:
            model = pickle.load(f)
        predictions = model.predict(test)
        resp_obj['valid'] = True
        resp_obj['prediction'] = str(predictions)
    else:
        resp_obj['valid'] = False
    return jsonify(resp_obj)

if __name__ == "__main__":
    app.run(debug=True)