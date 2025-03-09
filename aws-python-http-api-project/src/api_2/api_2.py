import json


def api2(event, context):
    body = {
        "attribute1" : "Python",
        "attribute2" : 200,
        "attribute3" : False,
        "attribute4" : 88.88,
        "attribute5" : "World",
        "attribute6" : 300,
        "attribute7" : True,
        "attribute8" : 77.77,
        "attribute9" : "MVC",
        "attribute10" : 500,
    }

    response = {"statusCode": 200, "body": json.dumps(body)}

    return response