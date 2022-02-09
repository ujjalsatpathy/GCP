def greet(requests):
    req_args = requests.args

    if req_args and "name" in req_args:
        return f"Hello {req_args['name']}!"
    else:
        return "Sorry.No name provided!"
