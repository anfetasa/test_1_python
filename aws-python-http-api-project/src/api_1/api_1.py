import json


def api1(event, context):
    body = {
        "attribute1" : "FastAPI",
        "attribute2" : 100,
        "attribute3" : True,
        "attribute4" : 99.99,
        "attribute5" : "Hello",
    }

    response = {"statusCode": 200, "body": json.dumps(body)}

    return response
