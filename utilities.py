
def validate(json, *keys):
    for key in keys:
        if not json or key not in json:
            return False
    return True
