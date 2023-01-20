from flask import Flask, jsonify, request, render_template
from flask_restful import Resource, Api
from pydantic import BaseModel
from churn_model.predict import make_prediction
import json
import typing as t

app = Flask(__name__)
api = Api(app)

prefix = 'v1'


class InputConfig(BaseModel):

    inputs: t.List[t.Dict]


class health(Resource):

    def get(self):

        return jsonify({"status": 200})


class predict(Resource):

    def get(self):

        return jsonify({'FIND PREDICTION FOR CHURN': 'POST'})

    def post(self):

        data = request.get_json()

        data = json.loads(data)

        data = InputConfig(inputs=data).inputs
        results = make_prediction(input_data=data)
        results['predictions'] = str(results['predictions'])

        return jsonify(results)


'''
x = load_dataset(filename=config.app_config.x_train).head(5)
xx = x.to_dict(orient='records')

r = requests.post('http://127.0.0.1:5000/predict',json=json.dumps(xx))
r = r.json()

import ast

d= ast.literal_eval(r['predictions'])



'''


api.add_resource(health, f'/{prefix}/health')
api.add_resource(predict, f'/{prefix}/predict')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
