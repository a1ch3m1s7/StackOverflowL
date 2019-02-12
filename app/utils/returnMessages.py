def error(StatusCode, msg):
    return {
        "status": StatusCode,
        "error": msg
       }

def success(StatusCode, data):
    return {
        "status" : StatusCode,
        "error" : data
    }

