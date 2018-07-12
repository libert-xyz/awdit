from chalice import Chalice
import json
import logging
import boto3
from botocore.exceptions import ClientError
from chalicelib.aws import ec2_list,health
app = Chalice(app_name='awdit')

# Enable DEBUG logs.
app.log.setLevel(logging.DEBUG)


@app.route('/')
def index():
    return health()

@app.route('/ec2-list')
def report():
    return ec2_list()


@app.route('/health')
def health_fn():
    return health()


# @app.route('/cloudwatch', methods=['POST'])
# def cloudwatch


# The view function above will return {"hello": "world"}
# whenever you make an HTTP GET request to '/'.
#
# Here are a few more examples:
#
# @app.route('/hello/{name}')
# def hello_name(name):
#    # '/hello/james' -> {"hello": "james"}
#    return {'hello': name}
#
# @app.route('/users', methods=['POST'])
# def create_user():
#     # This is the JSON body the user sent in their POST request.
#     user_as_json = app.current_request.json_body
#     # We'll echo the json body back to the user in a 'user' key.
#     return {'user': user_as_json}
#
# See the README documentation for more examples.
#
