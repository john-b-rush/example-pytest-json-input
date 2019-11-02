"""
Example greeting function we're testing
"""


def greeter(name: str) -> str:
    """
    Takes a name and returns a greeting
    """

    if len(name) > 8:
        return f"Hello {name}, you've got a very long name!"

    if len(name) % 2 == 0:
        return f"Hi {name}!"

    return f"Howdy {name}!"
