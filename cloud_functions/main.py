import functions_framework
import flask
import requests


def get_users(request):
    users = requests.get('https://gorest.co.in/public/v2/users').json()
    return flask.jsonify(users)


@functions_framework.cloud_event
def hello_cloud_event(cloud_event):
    print(f"Received event with ID: {cloud_event['id']} and data {cloud_event.data}")
