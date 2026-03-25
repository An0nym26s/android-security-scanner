def validate_input(data):
    """
    Validate the input data.
    """
    if not data:
        raise ValueError("Input data should not be empty.")
    return True


def parse_json(json_string):
    """
    Parse a JSON string and return a dictionary.
    """
    import json
    try:
        return json.loads(json_string)
    except json.JSONDecodeError as e:
        raise ValueError("Invalid JSON: " + str(e))


def handle_error(error):
    """
    Handle errors by logging or raising custom exceptions.
    """
    print(f'Error occurred: {error}')
    # Additional logging can be added here.
