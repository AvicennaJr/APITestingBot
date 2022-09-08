import requests
import json

urk = "http://pycon.fuadhabib.xyz/api/speakers/"


def get_response(url, headers, params):
    response = requests.get(url, headers=headers, params=params)

    unformatted_json = response.json()

    formatted_json = json.dumps(unformatted_json, indent=2)

    return formatted_json + f"\n\nRequested URL: {response.request.url}"


def post_response(url, headers, data):
    response = requests.post(url, headers=headers, data=data)

    unformatted_json = response.json()

    formatted_json = json.dumps(unformatted_json, indent=2)

    return formatted_json + f"\n\nRequested URL: {response.request.url}"


def update_response(url, headers, data):
    response = requests.put(url, headers=headers, data=data)

    unformatted_json = response.json()

    formatted_json = json.dumps(unformatted_json, indent=2)

    return formatted_json + f"\n\nRequested URL: {response.request.url}"


def delete_response(url, headers):
    response = requests.delete(url, headers=headers)

    unformatted_json = response.json()

    formatted_json = json.dumps(unformatted_json, indent=2)

    return formatted_json + f"\n\nRequested URL: {response.request.url}"
