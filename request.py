"""
https://github.com/gokavak/lambda-docker-image-pytorch-xgboost#4-get-predictions

robin@MacBook-Pro lambda-pytorch-example % python3 request.py
<Response [200]>
{'body': '[["Samoyed, Samoyede", 83.03044128417969], ["Pomeranian", '
         '6.9887542724609375], ["keeshond", 1.2964081764221191], ["collie", '
         '1.0797758102416992], ["Great Pyrenees", 0.9886764883995056]]',
 'statusCode': 200}
"""

import requests
import json
import pprint


headers = {
    "Content-Type": "application/json",
}

data = {
    "input_url": "https://github.com/pytorch/hub/raw/master/images/dog.jpg",
    "n_predictions": 5,
}

# data = {
#     "foo": "bar"
# }

response = requests.post(
    "http://localhost:9000/2015-03-31/functions/function/invocations",
    headers=headers,
    data=json.dumps(data),
)

print(response)

pprint.pprint(response.json())
