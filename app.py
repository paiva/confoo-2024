import os
import json
import requests
from flask import Flask, jsonify
from loguru import logger


API_GATEWAY = os.environ.get("API_GATEWAY_URL")
ENDPOINT = "users"

app = Flask(__name__)


@app.route("/")
def hello():
    logger.info("Got GET request on `/` endpoint")
    return "Hello, Confoo!"


@app.route("/users")
def get_users():
    logger.info("Got GET request on `/users` endpoint")
    endpoint_url = f"{API_GATEWAY}/{ENDPOINT}"
    try:
        # Make GET request to API Gateway endpoint
        response = requests.get(endpoint_url)

        # Check if request was successful (status code 200)
        if response.status_code == 200:
            # Parse JSON response
            users = response.json()
            logger.info("Users retrieved from API Gateway:")
            logger.info(json.dumps(users, indent=4))
            return jsonify(users)
        else:
            logger.error(
                f"Failed to retrieve users. Status code: {response.status_code}"
            )
    except Exception as e:
        logger.error(f"An error occurred: {str(e)}")
