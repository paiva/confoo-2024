# Introduction to AWS Lambda Functions

This is a simple flask application that talks to a Lambda function in AWS, makes a GET Request to get the number of users and returns it

### Dependencies

This repo assumes you are working with Python +3.8 and that you have pip3 and/or Poetry installed.

Create venv:

```
python3 -m venv venv
```

Then activate:

```
source venv/bin/activate
```

To install requirements with Poetry:

```
poetry install
```

or with pip3:

```
pip3 install -r requirements.txt
```

### The .env file

This application also assumes you have a `.env` file in the same folder. The contents of this file look like this:

```
export FLASK_APP=app
export FLASK_ENV=development
export API_GATEWAY_URL="https://<API_GATEWAY_TOKEN>.execute-api.<AWS_REGION>.amazonaws.com/<STAGE>"
```
