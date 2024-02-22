import os
import json
import requests
from flask import Flask, jsonify, request, render_template
from loguru import logger


API_GATEWAY = os.environ.get("API_GATEWAY_URL")
GET_USERS_ENDPOINT = "users"
ADD_USER_ENDPOINT = "add_user"

app = Flask(__name__)


@app.route("/")
def hello():
    logger.info("Got GET request on `/` endpoint")
    return "Hello, Confoo!"


@app.route("/users")
def get_users():
    logger.info("Got GET request on `/users` endpoint")
    endpoint_url = f"{API_GATEWAY}/{GET_USERS_ENDPOINT}"
    try:
        # Make GET request to API Gateway endpoint
        response = requests.get(endpoint_url)

        # Check if request was successful (status code 200)
        if response.status_code == 200:
            # Parse JSON response
            users = response.json().get("body")
            logger.info("Users retrieved from API Gateway:")
            logger.info(users)
            return users
        else:
            logger.error(
                f"Failed to retrieve users. Status code: {response.status_code}"
            )
    except Exception as e:
        logger.error(f"An error occurred: {str(e)}")


@app.route("/add_user")
def add_user():
    logger.info("Got GET request on `add_user` endpoint")
    return render_template("new_user.html")


@app.route("/add_new_user", methods=["POST"])
def add_new_user():
    logger.info("Got POST request on `/add_new_user` endpoint")

    form_data = request.form.to_dict()

    endpoint_url = f"{API_GATEWAY}/{ADD_USER_ENDPOINT}"
    logger.info(form_data)
    # Make a POST request to the Lambda function via API Gateway
    # Pass the dictionary to `json`, letting `requests` handle the conversion
    response = requests.post(
        endpoint_url, json=form_data, headers={"Content-Type": "application/json"}
    )

    logger.info(response)

    # Check if the request was successful
    if response.status_code == 200:
        return jsonify({"message": "User created successfully"}), 200
    else:
        # Handle error responses
        return (
            jsonify({"message": "Failed to create user", "error": response.text}),
            response.status_code,
        )
