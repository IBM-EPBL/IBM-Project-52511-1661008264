from flask import Flask
from flask import request, json
app = Flask(_name_)

:
@app.route('/models/MyEndpointSpec/<string:inputParam>', methods=['GET','POST',])
def model_api(inputParam):
    #api code
      :
                response = app.response_class(
                response=json.dumps(data,
                status=200,
                mimetype='application/json')
                return response